#!/usr/bin/env python3
"""Build a review workbook: one sheet per model, one row per conversation, one column per
setting plus the headline fields, in plain language. A cell is pale blue where its answer
matches the answer most models gave to that question (the modal answer over all accepted
conversations of all models) and yellow where it differs, so disagreement is visible at a
glance. A Summary sheet compares the models side by side with the same colouring.

Usage: python3 review_workbook.py [--out paper/review_workbook.xlsx]
"""
from __future__ import annotations

import argparse
import glob
import json
from collections import Counter, defaultdict
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from tunemybg_repro.summary import parse_composite, parse_value

ORDER = [("real_gemini36flash_50", "Gemini 3.6 Flash"), ("real_gemini31pro_50", "Gemini 3.1 Pro"),
         ("real_gemini35flashlite_50", "Gemini 3.5 Flash-Lite"), ("real_gpt56sol_med_50", "GPT-5.6-sol"),
         ("real_gpt54mini_med_50", "GPT-5.4-mini"), ("real_opus5", "Claude Opus 5"),
         ("real_sonnet5_20", "Claude Sonnet 5"), ("real_haiku45_50", "Claude Haiku 4.5"),
         ("real_deepseek_v4pro_50", "DeepSeek V4 Pro"), ("real_grok46_50", "Grok 4.6"),
         ("real_llama4maverick_50", "Llama 4 Maverick")]

SAME = PatternFill("solid", fgColor="DDEBF7")     # pale blue
DIFF = PatternFill("solid", fgColor="FFF2CC")     # yellow
HEAD = PatternFill("solid", fgColor="D9D9D9")
GREY = Font(color="808080")
BOLD = Font(bold=True)

OUTCOME = {"accepted_first_pass": "accepted first paste", "accepted_after_correction": "accepted after repair",
           "rejected_no_prompt": "rejected, no prompt offered", "rejected_schema_stop": "rejected, schema stop",
           "rejected_after_correction": "still rejected after repair"}


def short(key: str) -> str:
    return (key.replace("profile.", "").replace("aaps.core.", "").replace("aaps.dynisf.", "dynisf ")
            .replace("_00", ":00").replace(".", " ").replace("_", " "))


def cell_value(row: dict) -> str:
    d = row.get("decision")
    if d != "change":
        return d or "?"
    cur, sug = parse_composite(row.get("current_value")), parse_composite(row.get("suggested_value"))
    if len(sug) > 1 or len(cur) > 1:
        parts = [f"{k.replace('_', ' ')} {v}" for k, v in sug.items() if v != cur.get(k)]
        return "change: " + ("; ".join(parts) if parts else str(row.get("suggested_value"))[:60])
    return f"change: {row.get('suggested_value')}"


def norm(v: str) -> str:
    """Normalise an answer for the same/different comparison: decision plus numeric value."""
    if not v.startswith("change"):
        return v
    nums = []
    for tok in str(v).replace(";", " ").split():
        n = parse_value(tok)[0]
        if n is not None:
            nums.append(f"{n:g}")
    return "change " + " ".join(nums)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=Path("paper/review_workbook.xlsx"))
    args = ap.parse_args()

    # Load everything first so the cross-model modal answer per question is known.
    data: dict[str, list[dict]] = {}
    setting_keys: list[str] = []
    for exp, _ in ORDER:
        rows = []
        for p in sorted(glob.glob(f"results/{exp}/run_*/meta.json")):
            m = json.loads(Path(p).read_text(encoding="utf-8"))
            if m.get("status") != "completed":
                continue
            rec: dict = {"run": Path(p).parent.name, "outcome": OUTCOME.get(m.get("app_outcome"), m.get("app_outcome")),
                         "accepted": bool((m.get("validation") or {}).get("app_accepted"))}
            if rec["accepted"]:
                o = json.loads((Path(p).parent / "final.json").read_text(encoding="utf-8"))
                for r in o.get("parameter_decisions", []):
                    if isinstance(r, dict) and r.get("parameter_key"):
                        rec[r["parameter_key"]] = cell_value(r)
                        if r["parameter_key"] not in setting_keys:
                            setting_keys.append(r["parameter_key"])
                pr = o.get("profile_recommendation") or {}
                rec["focus"] = pr.get("focus")
                rec["profile decision"] = pr.get("decision")
                rec["confidence"] = pr.get("confidence")
                ms = next((s for s in o.get("analysis_steps", []) if isinstance(s, dict)
                           and s.get("key") == "meal_bolus_strategy"), {})
                rec["meal step"] = ms.get("status")
                recs = [x for x in o.get("recommendations", []) if isinstance(x, dict)]
                rec["first recommendation"] = (recs[0].get("title") or recs[0].get("area")) if recs else None
            rows.append(rec)
        data[exp] = rows

    extra_cols = ["focus", "profile decision", "confidence", "meal step"]
    columns = setting_keys + extra_cols

    # Modal answer per question over all accepted conversations of all models.
    modal: dict[str, str] = {}
    for col in columns:
        c = Counter(norm(str(rec[col])) for rows in data.values() for rec in rows
                    if rec["accepted"] and rec.get(col) is not None)
        if c:
            modal[col] = c.most_common(1)[0][0]

    wb = Workbook()

    # Summary sheet: one row per model, the modal answer that model gave to each question.
    ws = wb.active
    ws.title = "Summary"
    ws.append(["Model", "Conversations", "Accepted"] + [short(c) for c in columns])
    for exp, name in ORDER:
        rows = data[exp]
        acc = [r for r in rows if r["accepted"]]
        line = [name, len(rows), len(acc)]
        fills = [None, None, None]
        for col in columns:
            c = Counter(norm(str(r[col])) for r in acc if r.get(col) is not None)
            if not c:
                line.append("")
                fills.append(None)
                continue
            top, n = c.most_common(1)[0]
            disp = Counter(str(r[col]) for r in acc if r.get(col) is not None).most_common(1)[0][0]
            line.append(f"{disp}  ({n}/{len(acc)})" if len(c) > 1 or n < len(acc) else disp)
            fills.append(SAME if top == modal.get(col) else DIFF)
        ws.append(line)
        for j, f in enumerate(fills, start=1):
            if f:
                ws.cell(row=ws.max_row, column=j).fill = f

    # One sheet per model.
    for exp, name in ORDER:
        s = wb.create_sheet(name[:31])
        s.append(["Conversation", "App outcome"] + [short(c) for c in columns] + ["First recommendation"])
        for rec in data[exp]:
            line = [rec["run"], rec["outcome"]]
            fills: list = [None, None]
            for col in columns:
                v = rec.get(col)
                line.append("" if v is None else str(v))
                fills.append(None if (not rec["accepted"] or v is None)
                             else (SAME if norm(str(v)) == modal.get(col) else DIFF))
            line.append(rec.get("first recommendation") or "")
            s.append(line)
            r = s.max_row
            for j, f in enumerate(fills, start=1):
                if f:
                    s.cell(row=r, column=j).fill = f
            if not rec["accepted"]:
                for j in range(1, len(line) + 1):
                    s.cell(row=r, column=j).font = GREY

    # Legend + formatting on every sheet.
    for s in wb.worksheets:
        for c in s[1]:
            c.font = BOLD
            c.fill = HEAD
            c.alignment = Alignment(wrap_text=True, vertical="top")
        s.freeze_panes = "C2"
        widths = {1: 18, 2: 24} if s.title != "Summary" else {1: 20, 2: 13, 3: 10}
        for j in range(1, s.max_column + 1):
            s.column_dimensions[get_column_letter(j)].width = widths.get(j, 16)
        n = s.max_row + 2
        s.cell(row=n, column=1, value="pale blue: same answer as most models gave to this question "
               "(modal answer over all accepted conversations of all models)").fill = SAME
        s.cell(row=n + 1, column=1, value="yellow: a different answer from the one most models gave").fill = DIFF
        s.cell(row=n + 2, column=1, value="grey row: the app rejected this conversation; no answer reached the user")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(args.out)
    print("wrote", args.out, "| sheets:", ", ".join(w.title for w in wb.worksheets))


if __name__ == "__main__":
    main()
