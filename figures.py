#!/usr/bin/env python3
"""Paper figures.

Figure 1: the app's workflow as replicated (package -> four prompts -> LLM -> JSON -> app check
          -> repair prompt or result).
Figure 2: suggested values by model for the settings any model changed often, as strip plots
          against the current value and the AndroidAPS code default.

Outputs PNG (300 dpi) and PDF into paper/figures/.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from tunemybg_repro.summary import parse_composite, parse_value  # noqa: E402

OUT = Path("paper/figures")
OUT.mkdir(parents=True, exist_ok=True)

# reference palette (dataviz skill): surface, inks, slot-1 blue, slot-2 orange
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLUE, ORANGE = "#2a78d6", "#eb6834"
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
                     "font.size": 8.5, "axes.edgecolor": AXIS, "axes.linewidth": 0.8, "xtick.color": MUTED,
                     "ytick.color": INK2, "axes.labelcolor": INK2, "text.color": INK, "figure.facecolor": SURFACE,
                     "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE})

MODELS = [  # experiment dir, display label
    ("real_gemini36flash_50", "Gemini 3.6 Flash"), ("real_gemini31pro_50", "Gemini 3.1 Pro"),
    ("real_gemini35flashlite_50", "Gemini 3.5 Flash-Lite"), ("real_gpt56sol_med_50", "GPT-5.6-sol (medium)"),
    ("real_gpt54mini_med_50", "GPT-5.4-mini (medium)"), ("real_opus5", "Claude Opus 5"),
    ("real_sonnet5_20", "Claude Sonnet 5"), ("real_haiku45_50", "Claude Haiku 4.5"),
    ("real_deepseek_v4pro_50", "DeepSeek V4 Pro"), ("real_grok46_50", "Grok 4.6"),
    ("real_llama4maverick_50", "Llama 4 Maverick"),
]
# (parameter_key, component or '', title, unit, AAPS default numeric or None)
PANELS = [
    ("aaps.core.safety_limits", "max_iob_units", "Max IOB", "U", 3.0),
    ("aaps.core.safety_limits", "max_basal_u_per_hour", "Max basal", "U/h", 1.0),
    ("profile.target.00_00", "", "Target 00:00", "mg/dL", None),
    ("profile.basal.00_00", "", "Basal 00:00", "U/h", None),
    ("profile.isf.00_00", "", "ISF", "mg/dL/U", None),
    ("aaps.core.sensitivity", "dynamic_isf_adjustment_factor_percent", "Dynamic ISF factor", "%", 100.0),
]


def load_points(package: dict) -> dict[tuple[str, str], dict[str, tuple[list[float], int]]]:
    """(key, component) -> model label -> (suggested numeric values, n accepted runs)."""
    inv = {i["parameter_key"]: i for i in package["decision_inventory"]["items"]}
    out: dict = {p[:2]: {} for p in PANELS}
    for exp, label in MODELS:
        n = 0
        vals = {p[:2]: [] for p in PANELS}
        for d in sorted(Path("results", exp).glob("run_*")):
            mp, fp = d / "meta.json", d / "final.json"
            if not (mp.exists() and fp.exists()):
                continue
            m = json.loads(mp.read_text())
            if m.get("status") != "completed" or not (m.get("validation") or {}).get("app_accepted"):
                continue
            n += 1
            o = json.loads(fp.read_text())
            for row in o.get("parameter_decisions", []):
                if not isinstance(row, dict) or row.get("decision") != "change":
                    continue
                pk = row.get("parameter_key")
                for key, comp in vals:
                    if pk != key:
                        continue
                    item = inv[key]
                    if comp:
                        cur = next((c["current_value"] for c in item["components"] if c["key"] == comp), None)
                        sv = parse_composite(row.get("suggested_value")).get(comp)
                    else:
                        cur, sv = item["current_value"], row.get("suggested_value")
                    if sv is None or cur is None:
                        continue
                    v, _ = parse_value(sv)
                    c, _ = parse_value(cur)
                    if v is not None and c is not None and abs(v - c) > 1e-9:
                        vals[(key, comp)].append(v)
        for k in vals:
            out[k][label] = (vals[k], n)
    return out


def current_value(package: dict, key: str, comp: str) -> float:
    item = next(i for i in package["decision_inventory"]["items"] if i["parameter_key"] == key)
    s = next(c["current_value"] for c in item["components"] if c["key"] == comp) if comp else item["current_value"]
    return parse_value(s)[0]


def figure2(package: dict) -> None:
    pts = load_points(package)
    rng = np.random.default_rng(7)
    fig, axes = plt.subplots(2, 3, figsize=(7.2, 5.6), sharey=True)
    labels = [lab for _, lab in MODELS][::-1]
    for ax, (key, comp, title, unit, default) in zip(axes.flat, PANELS):
        cur = current_value(package, key, comp)
        ax.axvline(cur, color=INK, lw=1.0, zorder=1)
        if default is not None:
            ax.axvline(default, color=ORANGE, lw=1.0, zorder=1)
        for yi, lab in enumerate(labels):
            vals, n = pts[(key, comp)].get(lab, ([], 0))
            if vals:
                jitter = rng.uniform(-0.22, 0.22, len(vals))
                ax.scatter(vals, yi + jitter, s=18, color=BLUE, alpha=0.55, linewidths=1.2,
                           edgecolors=SURFACE, zorder=3)
            ax.text(1.0, yi, f"{len(vals)}/{n}", transform=ax.get_yaxis_transform(), ha="left", va="center",
                    fontsize=6.5, color=MUTED, clip_on=False)
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels, fontsize=7)
        ax.set_ylim(-0.7, len(labels) - 0.3)
        ax.set_title(f"{title} (current {cur:g} {unit})", fontsize=8.5, loc="left", color=INK)
        ax.set_xlabel(unit, color=MUTED)
        ax.grid(axis="x", color=GRID, lw=0.8)
        ax.set_axisbelow(True)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.tick_params(axis="y", length=0)
    # legend (two reference lines + one mark)
    from matplotlib.lines import Line2D
    handles = [Line2D([], [], color=BLUE, marker="o", lw=0, markersize=5, label="suggested value (one run)"),
               Line2D([], [], color=INK, lw=1.0, label="current value in the profile"),
               Line2D([], [], color=ORANGE, lw=1.0, label="AndroidAPS code default")]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, fontsize=7.5,
               bbox_to_anchor=(0.5, -0.01))
    fig.suptitle("Suggested values where a model proposed a change, by model (runs changed / runs accepted at right)",
                 fontsize=9, x=0.01, ha="left", color=INK)
    fig.tight_layout(rect=(0, 0.04, 1, 0.96))
    fig.savefig(OUT / "fig2_suggested_values.png", dpi=1000)
    fig.savefig(OUT / "fig2_suggested_values.pdf")
    plt.close(fig)


def figure1() -> None:
    fig, ax = plt.subplots(figsize=(7.2, 3.3))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 42)
    ax.axis("off")

    def box(x, y, w, h, text, fill=SURFACE, edge=AXIS, fs=7.3, bold=False):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1.2",
                                    fc=fill, ec=edge, lw=0.9, zorder=2))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=INK,
                fontweight="bold" if bold else "normal", linespacing=1.25, zorder=3)

    def arrow(x1, y1, x2, y2, color=INK2, ls="-"):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=9,
                                     color=color, lw=0.9, linestyle=ls, shrinkA=1, shrinkB=1, zorder=4))

    # lanes
    ax.add_patch(FancyBboxPatch((0.5, 22.5), 99, 17.5, boxstyle="round,pad=0.2", fc="none", ec=GRID, lw=0.8))
    ax.add_patch(FancyBboxPatch((0.5, 3), 99, 16, boxstyle="round,pad=0.2", fc="none", ec=GRID, lw=0.8))
    ax.text(2, 38.6, "TuneMyBG app", fontsize=7.2, color=MUTED, va="center")
    ax.text(2, 17.6, "User's chosen LLM (new chat)", fontsize=7.2, color=MUTED, va="center")

    # app lane
    box(3, 27, 17, 8, "Nightscout data and\nAAPS profile become\na JSON package")
    box(24, 27, 15, 8, "Prompts 1 to 4\n(fixed text)")
    box(43, 27, 15, 8, "Invalid JSON or\nrequired field missing:\nno prompt, dead end", fs=6.4)
    box(61, 27, 16, 8, "Paste result;\napp checks it")
    box(81, 31.5, 17, 5.5, "Analysis result\nscreen", fill="#eef3fb", edge=BLUE, bold=True)
    box(81, 24, 17, 5.5, "Repair prompt\n(three error types)")

    # LLM lane
    box(3, 6, 17, 8, "Attach package\nand Prompt 1")
    box(24, 6, 15, 8, "Prompt 2, then 3,\nafter each reply")
    box(43, 6, 15, 8, "Prompt 4:\nstrict JSON")
    box(62, 6, 16, 8, "Repair prompt:\nJSON again", edge=ORANGE)

    arrow(20, 31, 24, 31)                       # package to prompts
    arrow(11.5, 27, 11.5, 14)                   # package down to the conversation
    arrow(31.5, 27, 31.5, 14)                   # prompts down to the conversation
    arrow(20, 10, 24, 10)
    arrow(39, 10, 43, 10)
    arrow(51, 14, 66, 27)                       # JSON up to the check
    arrow(61, 31, 58, 31)                       # dead end
    arrow(77, 33, 81, 34)                       # accepted
    arrow(77, 29, 81, 27)                       # repair
    arrow(89, 24, 72, 14, color=ORANGE)         # repair prompt to the conversation
    arrow(76, 14, 74, 27, color=ORANGE, ls=(0, (2, 2)))   # corrected JSON back to the check
    ax.text(77.3, 35.6, "accepted", fontsize=6.3, color=MUTED)
    ax.text(77.6, 25.6, "repair", fontsize=6.3, color=MUTED)
    ax.text(1, 0.4, "Harness: identical package and prompts, 20 to 50 fresh conversations per model, provider-default "
                    "sampling; the app's acceptance rules reproduced and verified against the app.", fontsize=6.3, color=INK2)
    fig.tight_layout()
    fig.savefig(OUT / "fig1_workflow.png", dpi=1000)
    fig.savefig(OUT / "fig1_workflow.pdf")
    plt.close(fig)


if __name__ == "__main__":
    package = json.loads(Path.home().joinpath("Downloads", "TuneMyBG-analysis.json").read_text())
    figure1()
    figure2(package)
    print("wrote", sorted(p.name for p in OUT.iterdir()))
