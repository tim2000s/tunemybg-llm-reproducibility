#!/usr/bin/env python3
"""Replay the app's exact repair prompt for runs whose first pass needed one.

Rebuilds each conversation from transcript.json (package attachment + prompts 1-4 + the
model's own replies), sends the app-faithful repair prompt as a fresh turn, overwrites the
correction turn and attempt-1 artefacts, then re-validates. Only runs whose first pass is in
the app's "repair prompt" class are touched; accepted, invalid-JSON and schema-stop runs are not.

Usage: python3 rerun_corrections.py --backend openai_compat --base-url https://openrouter.ai/api/v1 \
           --model meta-llama/llama-4-maverick results/real_llama4maverick_50
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from revalidate import revalidate_run
from run_experiment import DEFAULT_PACKAGE, DEFAULT_PROMPTS
from tunemybg_repro.backends import BACKENDS
from tunemybg_repro.extract import extract_json, validate
from tunemybg_repro.prompts import correction_prompt, load_inputs


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("experiment", type=Path)
    ap.add_argument("--backend", required=True, choices=sorted(BACKENDS))
    ap.add_argument("--model", required=True)
    ap.add_argument("--base-url")
    ap.add_argument("--reasoning-effort")
    ap.add_argument("--max-tokens", type=int, default=32000)
    ap.add_argument("--package", type=Path, default=DEFAULT_PACKAGE)
    ap.add_argument("--prompts", type=Path, default=DEFAULT_PROMPTS)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    inputs = load_inputs(args.package, args.prompts)
    package = json.loads(inputs.package_text)
    kw = {"model": args.model, "max_tokens": args.max_tokens}
    if args.backend in ("openai", "openai_compat", "lmstudio"):
        kw["base_url"] = args.base_url or ("https://api.openai.com/v1" if args.backend == "openai" else "http://localhost:1234/v1")
        if args.backend == "openai":
            kw["max_tokens_param"] = "max_completion_tokens"
        if args.reasoning_effort:
            kw["reasoning_effort"] = args.reasoning_effort
    if args.backend == "anthropic":
        kw["fallbacks"] = args.model.startswith(("claude-opus-5", "claude-fable-5"))
    backend = BACKENDS[args.backend](**kw)

    todo = []
    for run_dir in sorted(args.experiment.glob("run_*")):
        meta_path = run_dir / "meta.json"
        if not meta_path.exists():
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if meta.get("status") != "completed" or meta.get("correction_replayed_with_app_wording"):
            continue
        raw = (run_dir / "final_raw.txt").read_text(encoding="utf-8")
        obj, method = extract_json(raw)
        if obj is None or method == "raw_decode_prefix":
            continue
        val = validate(obj, package)
        if not val["app_needs_repair"]:
            continue
        todo.append((run_dir, val))
    print(f"{len(todo)} run(s) need an app-style repair turn in {args.experiment.name}")
    if args.dry_run:
        for run_dir, val in todo:
            print(" ", run_dir.name, "->", correction_prompt(val["sections"], validation=val).splitlines()[1])
        return

    for run_dir, val in todo:
        transcript = json.loads((run_dir / "transcript.json").read_text(encoding="utf-8"))
        analysis_turns = [t for t in transcript if t.get("kind", "analysis") == "analysis"]
        conv = backend.new_conversation()
        for i, t in enumerate(analysis_turns):
            attachment = (inputs.package_path.name, inputs.package_text) if i == 0 else None
            conv.messages.append({"role": "user", "content": conv._user_content(t["prompt"], attachment)})
            conv.messages.append({"role": "assistant", "content": t["response"]})
        prompt = correction_prompt(val["sections"], validation=val)
        print(f"  [{run_dir.name}] repair: {prompt.splitlines()[1][:100]} ...", flush=True)
        turn = conv.send(prompt)
        print(f"  [{run_dir.name}] done in {turn.latency_s:.0f}s ({len(turn.text)} chars)", flush=True)
        # overwrite the correction turn and attempt-1 artefacts
        transcript = analysis_turns + [{"turn": len(analysis_turns) + 1, "kind": "correction", "prompt": prompt,
                                        "attachment": False, "response": turn.text,
                                        "latency_s": round(turn.latency_s, 2), "finish_reason": turn.finish_reason,
                                        "usage": turn.usage, "model_reported": turn.model_reported,
                                        "extra": turn.extra, "replayed": True}]
        (run_dir / "transcript.json").write_text(json.dumps(transcript, indent=2, ensure_ascii=False), encoding="utf-8")
        (run_dir / "final_raw_attempt1.txt").write_text(turn.text, encoding="utf-8")
        for extra in run_dir.glob("final_raw_attempt[2-9].txt"):
            extra.unlink()
        meta = json.loads((run_dir / "meta.json").read_text(encoding="utf-8"))
        meta["turns"] = meta["turns"][:len(analysis_turns)] + [{"turn": len(analysis_turns) + 1, "kind": "correction",
                                                                 "latency_s": round(turn.latency_s, 2),
                                                                 "finish_reason": turn.finish_reason,
                                                                 "usage": turn.usage, "response_chars": len(turn.text),
                                                                 "replayed": True}]
        meta["correction_replayed_with_app_wording"] = True
        (run_dir / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
        outcome = revalidate_run(run_dir, package)
        print(f"  [{run_dir.name}] outcome: {outcome}", flush=True)


if __name__ == "__main__":
    main()
