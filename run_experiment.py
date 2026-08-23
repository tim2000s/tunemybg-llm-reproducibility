#!/usr/bin/env python3
"""Run the TuneMyBG 4-prompt sequence N times in fresh conversations and save every output.

Examples:
  python3 run_experiment.py --backend mock --runs 5 --experiment smoke
  python3 run_experiment.py --backend lmstudio --model qwen/qwen3.5-9b --runs 10 --experiment qwen9b
  python3 run_experiment.py --backend ollama --model ministral-3:14b --runs 10 --experiment ministral
  python3 run_experiment.py --backend gemini --model gemini-3.6-flash --runs 10 --workers 2 --experiment gemini36flash
  python3 run_experiment.py --backend anthropic --model claude-opus-5 --runs 10 --experiment opus5
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from tunemybg_repro.backends import BACKENDS, MockBackend
from tunemybg_repro.prompts import CORRECTION_TEMPLATE, load_inputs
from tunemybg_repro.runner import run_experiment

HERE = Path(__file__).resolve().parent
DEFAULT_PACKAGE = Path.home() / "Downloads" / "TuneMyBG-analysis.json"
DEFAULT_PROMPTS = Path.home() / "Downloads" / "TuneMyBGPrompts.txt"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--backend", choices=sorted(BACKENDS), required=True)
    ap.add_argument("--model", help="model id for the backend (backend default if omitted)")
    ap.add_argument("--runs", type=int, default=5, help="number of fresh conversations")
    ap.add_argument("--experiment", required=True, help="name of the results sub-directory")
    ap.add_argument("--results-dir", type=Path, default=HERE / "results")
    ap.add_argument("--package", type=Path, default=DEFAULT_PACKAGE)
    ap.add_argument("--prompts", type=Path, default=DEFAULT_PROMPTS)
    ap.add_argument("--temperature", type=float, default=None,
                    help="sampling temperature; omitted = provider default (what the app user gets)")
    ap.add_argument("--max-tokens", type=int, default=32000)
    ap.add_argument("--timeout", type=float, default=3600, help="per-turn HTTP timeout in seconds")
    ap.add_argument("--workers", type=int, default=1, help="parallel conversations (API backends only)")
    ap.add_argument("--no-resume", action="store_true", help="re-run runs that already completed")
    ap.add_argument("--base-url", help="openai_compat/lmstudio/ollama server URL")
    ap.add_argument("--num-ctx", type=int, default=65536, help="ollama context window")
    ap.add_argument("--effort", help="anthropic output_config.effort (low|medium|high|xhigh|max)")
    ap.add_argument("--reasoning-effort", help="openai/openai_compat reasoning_effort (e.g. low|medium|high)")
    ap.add_argument("--no-fallbacks", action="store_true", help="anthropic: disable server-side refusal fallbacks")
    ap.add_argument("--max-repairs", type=int, default=1,
                    help="app-style correction rounds when the JSON fails validation (0 = none)")
    ap.add_argument("--correction-prompt", type=Path, default=None,
                    help="file with a custom correction template containing {sections}")
    ap.add_argument("--correct-unparseable", action="store_true",
                    help="also send a correction when the first pass is not valid JSON (the app does not)")
    args = ap.parse_args()

    inputs = load_inputs(args.package, args.prompts)
    package = json.loads(inputs.package_text)
    print(f"Loaded {len(inputs.prompts)} prompts from {inputs.prompts_path.name}; "
          f"package {inputs.package_path.name} ({len(inputs.package_text):,} chars, "
          f"sha256 {inputs.package_sha256[:12]})")

    common = {"temperature": args.temperature, "max_tokens": args.max_tokens, "timeout_s": args.timeout}
    cls = BACKENDS[args.backend]

    def make_backend(run_idx: int):
        kw = dict(common)
        if args.model:
            kw["model"] = args.model
        if cls is MockBackend:
            return MockBackend(package=package, seed=run_idx, **kw)
        if args.backend == "openai":
            kw.setdefault("model", "gpt-5")
            kw["base_url"] = args.base_url or "https://api.openai.com/v1"
            kw["max_tokens_param"] = "max_completion_tokens"
            kw["reasoning_effort"] = args.reasoning_effort
        elif args.backend in ("lmstudio", "openai_compat"):
            kw.setdefault("model", "qwen/qwen3.5-9b")
            if args.base_url:
                kw["base_url"] = args.base_url
            kw["reasoning_effort"] = args.reasoning_effort
        elif args.backend == "ollama":
            kw.setdefault("model", "ministral-3:14b")
            kw["num_ctx"] = args.num_ctx
            if args.base_url:
                kw["base_url"] = args.base_url
        elif args.backend == "anthropic":
            kw["effort"] = args.effort
            # server-side refusal fallbacks exist only on Opus 5 / Fable 5
            kw["fallbacks"] = (not args.no_fallbacks
                               and kw.get("model", "claude-opus-5").startswith(("claude-opus-5", "claude-fable-5")))
        return cls(**kw)

    template = (args.correction_prompt.read_text(encoding="utf-8").strip()
                if args.correction_prompt else CORRECTION_TEMPLATE)
    out_dir = args.results_dir / args.experiment
    results = run_experiment(inputs, make_backend, args.runs, out_dir, workers=args.workers,
                             resume=not args.no_resume, max_repairs=args.max_repairs,
                             correction_template=template, correct_unparseable=args.correct_unparseable)
    done = sum(1 for r in results if r["status"] == "completed")
    first_ok = sum(1 for r in results if (r.get("first_pass") or {}).get("fully_compliant"))
    final_ok = sum(1 for r in results if (r.get("validation") or {}).get("fully_compliant"))
    repaired = sum(1 for r in results if r.get("n_repairs"))
    print(f"\nFinished: {done}/{len(results)} completed; first-pass compliant {first_ok}, "
          f"needed correction {repaired}, compliant after correction {final_ok}. "
          f"Results in {out_dir}")
    print(f"Next: python3 analyse_runs.py {out_dir}")


if __name__ == "__main__":
    main()
