#!/usr/bin/env python3
"""One shareable graphic for the Diabettech article: the same record and prompts, a fresh
conversation each time, and what came back. Three panels: the maximum IOB limit every model
proposed in every accepted conversation (a barcode per model); DeepSeek's sensitivity factors;
and Gemini 3.6 Flash's headline, which forks between target and basal.

Writes paper/figures/fig_funky.png (2x) and .svg.
"""
from __future__ import annotations

import glob
import json
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.patches import Rectangle

from tunemybg_repro.summary import parse_composite, parse_value

ORDER = [("real_gemini36flash_50", "Gemini 3.6 Flash"), ("real_gemini31pro_50", "Gemini 3.1 Pro"),
         ("real_gemini35flashlite_50", "Gemini 3.5 Flash-Lite"), ("real_gpt56sol_med_50", "GPT-5.6"),
         ("real_gpt54mini_med_50", "GPT-5.4-mini"), ("real_opus5", "Claude Opus 5"),
         ("real_sonnet5_20", "Claude Sonnet 5"), ("real_haiku45_50", "Claude Haiku 4.5"),
         ("real_deepseek_v4pro_50", "DeepSeek V4 Pro"), ("real_grok46_50", "Grok 4.6"),
         ("real_llama4maverick_50", "Llama 4 Maverick")]
OUT = Path("paper/figures")
INK, MUTED, GRID = "#1b1b1b", "#6b6b6b", "#d9d9d9"
KEEP, REJECT = "#e6e6e6", "#ffffff"
TARGET, BASAL = "#2a6f97", "#e07a1f"


def runs(exp):
    out = []
    for p in sorted(glob.glob(f"results/{exp}/run_*/meta.json")):
        m = json.load(open(p))
        if m.get("status") != "completed":
            continue
        acc = bool((m.get("validation") or {}).get("app_accepted"))
        o = json.load(open(p.replace("meta.json", "final.json"))) if acc else None
        out.append((acc, o))
    return out


def max_iob(o):
    for r in o.get("parameter_decisions", []):
        if isinstance(r, dict) and r.get("parameter_key") == "aaps.core.safety_limits":
            if r.get("decision") != "change":
                return None
            v = parse_value(parse_composite(r.get("suggested_value")).get("max_iob_units"))[0]
            return v if v is not None and v != 25 else None
    return None


def isf(o):
    for r in o.get("parameter_decisions", []):
        if isinstance(r, dict) and r.get("parameter_key") == "profile.isf.00_00" and r.get("decision") == "change":
            return parse_value(r.get("suggested_value"))[0]
    return None


def main(paper=False):
    data = {e: runs(e) for e, _ in ORDER}
    fig = plt.figure(figsize=(10, 9.6 if paper else 10.4), dpi=100)
    fig.patch.set_facecolor("white")
    gs = fig.add_gridspec(3, 1, height_ratios=[11, 2.4, 1.6], hspace=0.42, left=0.2, right=0.97, top=(0.95 if paper else 0.87), bottom=(0.07 if paper else 0.06))

    if not paper:
      fig.text(0.03, 0.965, "Same record. Same prompts. A fresh conversation each time.", fontsize=19, fontweight="bold", color=INK, ha="left")
      fig.text(0.03, 0.935, "What eleven language models told one person with type 1 diabetes to do with their insulin pump settings,\n"
             "replaying a paid app's own workflow up to fifty times per model.", fontsize=10.5, color=MUTED, ha="left", va="top", linespacing=1.4)

    # Panel 1: barcode of max IOB
    ax = fig.add_subplot(gs[0])
    cmap = colors.LinearSegmentedColormap.from_list("iob", ["#08306b", "#2171b5", "#6baed6", "#c6dbef"])
    norm = colors.Normalize(vmin=2, vmax=20)
    for i, (e, name) in enumerate(ORDER):
        y = len(ORDER) - 1 - i
        for j, (acc, o) in enumerate(data[e]):
            if not acc:
                ax.add_patch(Rectangle((j, y + 0.12), 0.9, 0.76, facecolor=REJECT, edgecolor=GRID, lw=0.6, hatch="////"))
                continue
            v = max_iob(o)
            ax.add_patch(Rectangle((j, y + 0.12), 0.9, 0.76, facecolor=KEEP if v is None else cmap(norm(v)), edgecolor="white", lw=0.8))
        acc_runs = [max_iob(o) for acc, o in data[e] if acc]
        changed = [v for v in acc_runs if v is not None]
        note = "left alone" if not changed else f"{len(changed)} of {len(acc_runs)} lowered it, " + (f"{len(set(changed))} different values" if len(set(changed)) > 1 else "one value")
        ax.text(len(data[e]) + 0.6, y + 0.5, note, va="center", fontsize=8.5, color=MUTED)
        ax.text(-0.8, y + 0.5, name, va="center", ha="right", fontsize=10, color=INK)
    # one user, one draw
    j0 = 22
    ax.add_patch(Rectangle((j0 - 0.12, len(ORDER) - 1 + 0.02), 1.14, 0.96, facecolor="none", edgecolor=INK, lw=1.8, zorder=5))
    ax.plot([j0 + 0.45, j0 + 0.45], [len(ORDER) + 0.02, len(ORDER) + 0.42], color=INK, lw=1)
    ax.text(j0 + 0.45, len(ORDER) + 0.5, ("one conversation, as a user receives it" if paper else "a paying user gets one of these, and is not told which"), ha="center", va="bottom", fontsize=9.5, color=INK, fontweight="bold")
    ax.set_xlim(-0.3, 70)
    ax.set_ylim(-1.3, len(ORDER) + 1.15)
    ax.axis("off")
    ax.set_title("Maximum insulin on board limit each conversation proposed (current setting 25 U)", loc="left", fontsize=11.5, color=INK, pad=6, fontweight="bold")
    # legend
    lx, ly = 0.0, -1.0
    for k, (lab, col) in enumerate([("left at 25 U", KEEP), ("rejected by the app", REJECT)]):
        ax.add_patch(Rectangle((lx + k * 14, ly), 0.9, 0.6, facecolor=col, edgecolor=GRID, lw=0.6, hatch="////" if col == REJECT else None, clip_on=False))
        ax.text(lx + k * 14 + 1.3, ly + 0.3, lab, va="center", fontsize=8.5, color=MUTED, clip_on=False)
    for k, v in enumerate([2, 5, 8, 12, 20]):
        ax.add_patch(Rectangle((44 + k * 1.0, ly), 0.9, 0.6, facecolor=cmap(norm(v)), edgecolor="white", lw=0.6, clip_on=False))
    ax.text(43.2, ly + 0.3, "lowered to 2 U", ha="right", va="center", fontsize=8.5, color=MUTED, clip_on=False)
    ax.text(49.2, ly + 0.3, "lowered to 20 U", va="center", fontsize=8.5, color=MUTED, clip_on=False)

    # Panel 2: DeepSeek ISF strip
    ax2 = fig.add_subplot(gs[1])
    vals = [isf(o) for acc, o in data["real_deepseek_v4pro_50"] if acc]
    vals = [v for v in vals if v is not None]
    ax2.axvline(56, color=INK, lw=1.2)
    ax2.text(56, 1.55, "current: 56", ha="center", fontsize=8.5, color=INK)
    ax2.scatter(vals, [1] * len(vals), s=120, color="#2a6f97", alpha=0.55, edgecolor="white", lw=1, zorder=3)
    ax2.set_xlim(20, 190)
    ax2.set_ylim(0.3, 1.9)
    ax2.set_yticks([])
    ax2.set_xticks([30, 56, 80, 110, 140, 180])
    ax2.set_xlabel("mg/dl per unit", fontsize=9, color=MUTED, loc="right")
    ax2.tick_params(axis="x", labelsize=9, colors=MUTED, length=0)
    for s in ("top", "right", "left"):
        ax2.spines[s].set_visible(False)
    ax2.spines["bottom"].set_color(GRID)
    ax2.set_title("DeepSeek V4 Pro: sensitivity factor in the 20 conversations that changed it", loc="left", fontsize=11.5, color=INK, pad=10, fontweight="bold")
    ax2.text(183, 0.55, "one run doubles every correction;\nanother cuts it by two thirds", ha="right", fontsize=8.5, color=MUTED, va="bottom", linespacing=1.3)

    # Panel 3: Flash headline tiles
    ax3 = fig.add_subplot(gs[2])
    focus = [(o.get("profile_recommendation") or {}).get("focus") for acc, o in data["real_gemini36flash_50"] if acc]
    for j, f in enumerate(focus):
        ax3.add_patch(Rectangle((j, 0.2), 0.9, 0.8, facecolor=TARGET if f == "target" else BASAL, edgecolor="white", lw=0.8))
    ax3.set_xlim(-0.3, 70)
    ax3.set_ylim(0, 1.2)
    ax3.axis("off")
    nt = sum(1 for f in focus if f == "target")
    ax3.set_title("Gemini 3.6 Flash's headline recommendation, fifty conversations in order", loc="left", fontsize=11.5, color=INK, pad=10, fontweight="bold")
    ax3.text(51.2, 0.82, f"raise the overnight target ({nt})", color=TARGET, fontsize=9, va="center")
    ax3.text(51.2, 0.38, f"cut the midnight basal ({len(focus) - nt})", color=BASAL, fontsize=9, va="center")

    if not paper:
      fig.text(0.03, 0.012, "Street T, 2026. Eleven models, 490 conversations, one 14-day AndroidAPS record; each cell is one conversation.\nThe app's check accepted every coloured cell. diabettech.com",
             fontsize=8, color=MUTED, va="bottom", linespacing=1.4)
    OUT.mkdir(parents=True, exist_ok=True)
    if paper:
        fig.savefig(OUT / "fig3_conversations.png", dpi=1000)
        fig.savefig(OUT / "fig3_conversations.pdf")
        print("wrote", OUT / "fig3_conversations.png")
    else:
        fig.savefig(OUT / "fig_funky.png", dpi=200)
        fig.savefig(OUT / "fig_funky.svg")
        print("wrote", OUT / "fig_funky.png")


if __name__ == "__main__":
    import sys
    main(paper="--paper" in sys.argv)
