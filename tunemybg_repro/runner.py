"""Execute N independent 4-prompt conversations (plus the app's correction loop) and persist
everything per run."""

from __future__ import annotations

import json
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from .backends import Backend
from .extract import decision_diff, extract_json, validate
from .prompts import CORRECTION_TEMPLATE, Inputs, correction_prompt


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _record_turn(transcript, meta, i, prompt, turn, attachment: bool, kind: str):
    transcript.append({"turn": i, "kind": kind, "prompt": prompt, "attachment": attachment,
                       "response": turn.text, "latency_s": round(turn.latency_s, 2),
                       "finish_reason": turn.finish_reason, "usage": turn.usage,
                       "model_reported": turn.model_reported, "extra": turn.extra})
    meta["turns"].append({"turn": i, "kind": kind, "latency_s": round(turn.latency_s, 2),
                          "finish_reason": turn.finish_reason, "usage": turn.usage,
                          "response_chars": len(turn.text)})


def classify_attempts(attempts: list[dict[str, Any]]) -> tuple[dict[str, Any] | None, str | None]:
    """App-faithful outcome and the JSON the app would hold at the end.

    accepted_first_pass / accepted_after_correction: the app accepted that attempt.
    rejected_no_prompt: first pass not valid JSON ("Paste a valid JSON response from AI.").
    rejected_schema_stop: "does not match the TuneMyBG schema", no prompt.
    rejected_after_correction: repair prompt issued but the corrected paste still fails.
    The returned attempt is the accepted one, else the last attempt (for analysis only)."""
    if not attempts:
        return None, None
    first = attempts[0]
    if first["obj"] is None or first["extraction_method"] == "raw_decode_prefix":
        return attempts[-1], "rejected_no_prompt"
    if first["validation"]["app_accepted"]:
        return first, "accepted_first_pass"
    if first["validation"]["app_schema_stop"]:
        return attempts[-1], "rejected_schema_stop"
    for a in attempts[1:]:
        if a["obj"] is not None and a["extraction_method"] != "raw_decode_prefix" and a["validation"]["app_accepted"]:
            return a, "accepted_after_correction"
    return attempts[-1], "rejected_after_correction"


def _evaluate(run_dir: Path, text: str, package: dict, attempt: int) -> dict[str, Any]:
    """Extract + validate one final-JSON attempt (0 = first pass) and save its artefacts."""
    suffix = "" if attempt == 0 else f"_attempt{attempt}"
    (run_dir / f"final_raw{suffix}.txt").write_text(text, encoding="utf-8")
    obj, method = extract_json(text)
    validation = None
    if obj is not None:
        (run_dir / f"final{suffix}.json").write_text(json.dumps(obj, indent=2, ensure_ascii=False),
                                                     encoding="utf-8")
        validation = validate(obj, package)
    return {"attempt": attempt, "json_extracted": obj is not None, "extraction_method": method,
            "validation": validation, "obj": obj}


def run_one(run_idx: int, inputs: Inputs, backend: Backend, run_dir: Path,
            package: dict[str, Any], max_repairs: int = 1,
            correction_template: str = CORRECTION_TEMPLATE, verbose: bool = True,
            correct_unparseable: bool = False) -> dict[str, Any]:
    run_dir.mkdir(parents=True, exist_ok=True)
    run_id = run_dir.name
    meta: dict[str, Any] = {"run_id": run_id, "run_idx": run_idx, "started_at": _now(),
                            "backend": backend.describe(), "max_repairs": max_repairs,
                            "status": "running", "turns": [], "attempts": []}
    transcript: list[dict[str, Any]] = []
    conv = backend.new_conversation()
    attempts: list[dict[str, Any]] = []
    t_start = time.time()
    try:
        n_prompts = len(inputs.prompts)
        for i, prompt in enumerate(inputs.prompts, start=1):
            attachment = (inputs.package_path.name, inputs.package_text) if i == 1 else None
            if verbose:
                print(f"  [{run_id}] prompt {i}/{n_prompts} ...", flush=True)
            turn = conv.send(prompt, attachment=attachment)
            _record_turn(transcript, meta, i, prompt, turn, bool(attachment), "analysis")
            if verbose:
                print(f"  [{run_id}] prompt {i} done in {turn.latency_s:.0f}s "
                      f"({len(turn.text)} chars, finish={turn.finish_reason})", flush=True)

        attempts.append(_evaluate(run_dir, transcript[-1]["response"], package, 0))
        # App-style correction loop: ask for fixes until compliant or out of repairs
        while len(attempts) - 1 < max_repairs:
            last = attempts[-1]
            val = last["validation"]
            if val and val["app_accepted"]:
                break   # the app accepts it (prompt-only rule breaches are recorded, not repaired)
            if (val is None or last["extraction_method"] == "raw_decode_prefix") and not correct_unparseable:
                # The app shows "Paste a valid JSON response from AI." and offers no prompt
                if verbose:
                    print(f"  [{run_id}] first pass not valid JSON; app offers no correction", flush=True)
                break
            if val and val["app_schema_stop"]:
                # "The AI response does not match the TuneMyBG schema." and no prompt
                if verbose:
                    print(f"  [{run_id}] app schema stop: {val['failed_by_tier']['app_schema']}", flush=True)
                break
            sections = val["sections"] if val else []
            prompt = correction_prompt(sections, correction_template, last["validation"])
            n = len(transcript) + 1
            if verbose:
                print(f"  [{run_id}] correction {len(attempts)}/{max_repairs}: "
                      f"{', '.join(sections) or 'unparseable'} ...", flush=True)
            turn = conv.send(prompt)
            _record_turn(transcript, meta, n, prompt, turn, False, "correction")
            if verbose:
                print(f"  [{run_id}] correction done in {turn.latency_s:.0f}s "
                      f"({len(turn.text)} chars)", flush=True)
            attempts.append(_evaluate(run_dir, turn.text, package, len(attempts)))
        meta["status"] = "completed"
    except Exception as e:  # noqa: BLE001 - record every failure rather than abort the batch
        meta["status"] = "failed"
        meta["error"] = f"{type(e).__name__}: {e}"
        meta["traceback"] = traceback.format_exc()
        if verbose:
            print(f"  [{run_id}] FAILED: {meta['error']}", flush=True)
    finally:
        first = attempts[0] if attempts else None
        accepted, outcome = classify_attempts(attempts)
        meta["app_outcome"] = outcome
        meta["finished_at"] = _now()
        meta["wall_time_s"] = round(time.time() - t_start, 2)
        meta["attempts"] = [{k: v for k, v in a.items() if k != "obj"} for a in attempts]
        meta["n_repairs"] = max(len(attempts) - 1, 0)
        meta["first_pass"] = {"json_extracted": first["json_extracted"] if first else False,
                              "extraction_method": first["extraction_method"] if first else None,
                              "fully_compliant": bool(first and first["validation"]
                                                      and first["validation"]["fully_compliant"]),
                              "sections": (first["validation"] or {}).get("sections") if first else None}
        meta["json_extracted"] = bool(accepted and accepted["json_extracted"])
        meta["extraction_method"] = accepted["extraction_method"] if accepted else None
        meta["validation"] = accepted["validation"] if accepted else None
        meta["accepted_attempt"] = accepted["attempt"] if accepted else None
        meta["repair_diff"] = (decision_diff(first["obj"], accepted["obj"])
                               if first and accepted and accepted is not first else None)
        if accepted and accepted["obj"] is not None:
            (run_dir / "final.json").write_text(json.dumps(accepted["obj"], indent=2,
                                                           ensure_ascii=False), encoding="utf-8")
        if first and first["obj"] is not None:
            (run_dir / "final_firstpass.json").write_text(json.dumps(first["obj"], indent=2,
                                                                     ensure_ascii=False),
                                                          encoding="utf-8")
        (run_dir / "transcript.json").write_text(json.dumps(transcript, indent=2, ensure_ascii=False),
                                                 encoding="utf-8")
        (run_dir / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False),
                                           encoding="utf-8")
    return meta


def run_experiment(inputs: Inputs, make_backend: Callable[[int], Backend], n_runs: int,
                   out_dir: Path, workers: int = 1, resume: bool = True, max_repairs: int = 1,
                   correction_template: str = CORRECTION_TEMPLATE,
                   verbose: bool = True, correct_unparseable: bool = False) -> list[dict[str, Any]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    package = json.loads(inputs.package_text)
    probe = make_backend(0)
    exp_meta = {"experiment": out_dir.name, "created_at": _now(), "n_runs_requested": n_runs,
                "workers": workers, "backend": probe.describe(), "max_repairs": max_repairs,
                "correction_template": correction_template, "correct_unparseable": correct_unparseable,
                "package_path": str(inputs.package_path), "package_sha256": inputs.package_sha256,
                "prompts_path": str(inputs.prompts_path), "prompts_sha256": inputs.prompts_sha256,
                "n_prompts": len(inputs.prompts)}
    exp_file = out_dir / "experiment.json"
    if exp_file.exists() and resume:
        prev = json.loads(exp_file.read_text())
        if prev.get("package_sha256") != inputs.package_sha256 or \
           prev.get("prompts_sha256") != inputs.prompts_sha256:
            raise SystemExit(f"{exp_file} was created with different inputs; "
                             "use a new --experiment name")
        exp_meta["created_at"] = prev.get("created_at", exp_meta["created_at"])
    exp_file.write_text(json.dumps(exp_meta, indent=2), encoding="utf-8")

    todo = []
    for idx in range(1, n_runs + 1):
        run_dir = out_dir / f"run_{idx:03d}"
        meta_path = run_dir / "meta.json"
        if resume and meta_path.exists():
            try:
                if json.loads(meta_path.read_text()).get("status") == "completed":
                    continue
            except json.JSONDecodeError:
                pass
        todo.append((idx, run_dir))
    if verbose:
        print(f"Experiment '{out_dir.name}': {len(todo)} run(s) to execute "
              f"({n_runs - len(todo)} already complete), workers={workers}, "
              f"max_repairs={max_repairs}")

    def job(idx, run_dir):
        return run_one(idx, inputs, make_backend(idx), run_dir, package, max_repairs,
                       correction_template, verbose, correct_unparseable)

    results: list[dict[str, Any]] = []
    if workers <= 1:
        for idx, run_dir in todo:
            results.append(job(idx, run_dir))
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futs = [pool.submit(job, idx, run_dir) for idx, run_dir in todo]
            for f in as_completed(futs):
                results.append(f.result())
    return results
