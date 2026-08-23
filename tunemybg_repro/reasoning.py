"""Natural-language analysis of the reasoning in the final JSONs: which reasoning points are
shared by most runs and which vary, per setting and for the headline recommendation.

Method (no external NLP dependencies): split each text into sentences, build TF-IDF vectors
over unigrams+bigrams, greedily cluster sentences across runs by cosine similarity, and report
each cluster by the number of runs it appears in with a representative (medoid) sentence.
Also counts the concrete evidence tokens (numbers with units, clock times) cited per run."""

from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np

STOP = set("""a an the and or but if then than so as of to in on at by for from with without into onto
over under between within during after before while about against per via is are was were be been being
am do does did doing have has had having can could may might must shall should will would it its this
that these those there here where when which who whom whose what why how not no nor only own same such
too very s t just also both each few more most other some any all very same other such up down out off
again further once here there i me my we our you your he she they them their his her who this data run
runs value values setting settings current currently package given provided based using use used shows
show shown indicates indicating suggests suggest supports supported evidence because therefore thus
however although while despite rather instead across over within throughout""".split())

_SENT_SPLIT = re.compile(r"(?<=[.;!?])\s+(?=[A-Z0-9(])")
_TOKEN = re.compile(r"[a-z][a-z_/]+|\d+(?:\.\d+)?")
_EVIDENCE = re.compile(
    r"\b\d{1,2}:\d{2}\b|\b\d{1,2}\s?(?:am|pm)\b|\b\d+(?:\.\d+)?\s?(?:%|percent|mg/dl|mg/dL|u/h|U/h|u\b|U\b|h\b|hours?|min\b|minutes?|g/u|g/U)",
    re.IGNORECASE)


def _text(x: Any) -> str:
    """Models occasionally return a list where a string was specified; flatten it."""
    if isinstance(x, (list, tuple)):
        return " ".join(_text(i) for i in x)
    if isinstance(x, dict):
        return " ".join(_text(v) for v in x.values())
    return str(x or "")


def sentences(text: str) -> list[str]:
    text = " ".join(_text(text).split())
    return [s.strip() for s in _SENT_SPLIT.split(text) if len(s.strip()) > 15]


def tokens(text: str) -> list[str]:
    toks = [t for t in _TOKEN.findall(text.lower()) if t not in STOP and len(t) > 1]
    return toks + [f"{a}_{b}" for a, b in zip(toks, toks[1:])]


def evidence(text: str) -> set[str]:
    out = set()
    for m in _EVIDENCE.findall(_text(text)):
        e = re.sub(r"\s+", "", m.lower()).replace("percent", "%").replace("hours", "h").replace("hour", "h") \
            .replace("minutes", "min").replace("minute", "min")
        out.add(e)
    return out


class _Clusterer:
    def __init__(self, docs: list[list[str]], threshold: float = 0.25):
        self.threshold = threshold
        df = Counter(t for d in docs for t in set(d))
        n = max(len(docs), 1)
        self.vocab = {t: i for i, t in enumerate(df)}
        self.idf = np.array([math.log((1 + n) / (1 + df[t])) + 1 for t in self.vocab])
        self.X = np.zeros((len(docs), len(self.vocab)))
        for i, d in enumerate(docs):
            for t, c in Counter(d).items():
                self.X[i, self.vocab[t]] = c
        self.X *= self.idf
        norms = np.linalg.norm(self.X, axis=1, keepdims=True)
        norms[norms == 0] = 1
        self.X /= norms

    def cluster(self, order: list[int]) -> list[list[int]]:
        clusters: list[list[int]] = []
        centroids: list[np.ndarray] = []
        for i in order:
            best, best_sim = -1, self.threshold
            for c, cen in enumerate(centroids):
                sim = float(self.X[i] @ cen / (np.linalg.norm(cen) or 1))
                if sim > best_sim:
                    best, best_sim = c, sim
            if best == -1:
                clusters.append([i])
                centroids.append(self.X[i].copy())
            else:
                clusters[best].append(i)
                centroids[best] = self.X[clusters[best]].mean(axis=0)
        return clusters

    def medoid(self, members: list[int]) -> int:
        sub = self.X[members]
        sims = sub @ sub.T
        return members[int(np.argmax(sims.sum(axis=1)))]


def cluster_texts(items: list[tuple[str, str]], threshold: float = 0.25) -> list[dict[str, Any]]:
    """items: (run_id, text). Returns clusters sorted by number of runs covered."""
    sents: list[tuple[str, str]] = [(rid, s) for rid, text in items for s in sentences(text)]
    if not sents:
        return []
    docs = [tokens(s) for _, s in sents]
    cl = _Clusterer(docs, threshold)
    order = sorted(range(len(sents)), key=lambda i: -len(docs[i]))
    out = []
    for members in cl.cluster(order):
        run_ids = sorted({sents[i][0] for i in members})
        med = cl.medoid(members)
        out.append({"n_runs": len(run_ids), "n_sentences": len(members), "runs": run_ids,
                    "representative": sents[med][1],
                    "examples": [sents[i][1] for i in members[:3] if i != med][:2]})
    out.sort(key=lambda c: (-c["n_runs"], -c["n_sentences"]))
    return out


def _load(exp_dir: Path) -> list[dict[str, Any]]:
    runs = []
    for d in sorted(exp_dir.glob("run_*")):
        if (d / "final.json").exists() and (d / "meta.json").exists():
            meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
            if meta.get("status") == "completed":
                runs.append({"run_id": meta["run_id"],
                             "final": json.loads((d / "final.json").read_text(encoding="utf-8"))})
    return runs


def _slots(runs: list[dict[str, Any]], package: dict[str, Any]) -> dict[str, dict[str, list[tuple[str, str]]]]:
    """slot name -> group name -> [(run_id, text)]. Groups split contested decisions."""
    inv = {i["parameter_key"]: i for i in package["decision_inventory"]["items"]}
    slots: dict[str, dict[str, list[tuple[str, str]]]] = defaultdict(lambda: defaultdict(list))
    for r in runs:
        f, rid = r["final"], r["run_id"]
        for d in f.get("parameter_decisions", []):
            if isinstance(d, dict) and d.get("parameter_key") in inv:
                slots[f"decision: {inv[d['parameter_key']]['label']}"][d.get("decision") or "?"].append(
                    (rid, d.get("rationale") or ""))
        pr = f.get("profile_recommendation") or {}
        slots["profile recommendation"][pr.get("focus") or "?"].append(
            (rid, f"{pr.get('recommendation') or ''} {pr.get('rationale') or ''}"))
        recs = [x for x in f.get("recommendations", []) if isinstance(x, dict)]
        if recs:
            slots["primary recommendation"][recs[0].get("area") or "?"].append(
                (rid, f"{recs[0].get('title') or ''}. {recs[0].get('description') or ''}"))
        slots["summary"]["all"].append((rid, f.get("summary") or ""))
        slots["issues"]["all"].append((rid, " ".join(str(x) for x in f.get("issues") or [])))
        for s in f.get("analysis_steps", []):
            if isinstance(s, dict):
                slots[f"step findings: {s.get('key')}"]["all"].append((rid, s.get("findings") or ""))
        ms = f.get("meal_strategy_summary") or {}
        slots["meal strategy"]["all"].append((rid, f"{ms.get('suggestion') or ''} {ms.get('rationale') or ''}"))
    return slots


def shared_phrases(items: list[tuple[str, str]], min_frac: float = 0.5, max_n: int = 12) -> list[tuple[str, int]]:
    """2–3 word phrases present in at least min_frac of the runs (document frequency over runs)."""
    by_run: dict[str, set[str]] = defaultdict(set)
    for rid, text in items:
        toks = [t for t in _TOKEN.findall(_text(text).lower()) if len(t) > 1]
        for k in (2, 3):
            for i in range(len(toks) - k + 1):
                gram = toks[i:i + k]
                if gram[0] in STOP or gram[-1] in STOP or all(g.replace(".", "").isdigit() for g in gram):
                    continue
                by_run[rid].add(" ".join(gram))
    n = len(by_run)
    df = Counter(p for s in by_run.values() for p in s)
    out = [(p, c) for p, c in df.most_common() if c >= min_frac * n]
    # drop 2-grams fully contained in a 3-gram that is just as frequent
    keep = []
    for p, c in out:
        if any(p != q and p in q and cq >= c for q, cq in out):
            continue
        keep.append((p, c))
    return keep[:max_n]


def analyse_reasoning(exp_dir: Path, package: dict[str, Any], threshold: float = 0.25,
                      common_pct: float = 0.6, min_runs: int = 2) -> dict[str, Any]:
    runs = _load(exp_dir)
    n = len(runs)
    exp_meta = json.loads((exp_dir / "experiment.json").read_text(encoding="utf-8"))
    slots = _slots(runs, package)
    result = {"experiment": exp_dir.name, "model": exp_meta.get("backend", {}).get("model"), "n": n,
              "slots": []}
    for slot, groups in slots.items():
        entry = {"slot": slot, "groups": []}
        for group, items in groups.items():
            g_n = len({rid for rid, _ in items})
            clusters = cluster_texts(items, threshold)
            ev = Counter()
            for rid, text in items:
                for e in evidence(text):
                    ev[e] += 1
            entry["groups"].append({
                "group": group, "n_runs": g_n,
                "common": [c for c in clusters if c["n_runs"] >= common_pct * g_n and c["n_runs"] >= min_runs],
                "varying": [c for c in clusters if min_runs <= c["n_runs"] < common_pct * g_n],
                "unique": sum(1 for c in clusters if c["n_runs"] < min_runs),
                "evidence": ev.most_common(12),
                "phrases": shared_phrases(items),
            })
        entry["groups"].sort(key=lambda g: -g["n_runs"])
        result["slots"].append(entry)
    return result


def write_reasoning_report(res: dict[str, Any], out_md: Path, out_csv: Path | None = None,
                           max_varying: int = 6) -> Path:
    n = res["n"]
    L = [f"# Reasoning analysis — {res['model']} ({n} runs, `{res['experiment']}`)", "",
         "Each model rationale is split into sentences; sentences making the same point across runs are "
         "grouped. **Shared** = the point appears in at least 60% of the runs in that group; **varying** = "
         "it appears in some runs but not most. Counts are runs, not sentences. 'Evidence cited' lists the "
         "numbers and times the model quoted, with the number of runs quoting each.", ""]
    rows = []
    for s in res["slots"]:
        L += [f"## {s['slot']}", ""]
        for g in s["groups"]:
            title = f"{g['group']} — {g['n_runs']}/{n} runs" if g["group"] != "all" else f"{g['n_runs']} runs"
            L += [f"### {title}", ""]
            if g["common"]:
                L += ["**Shared reasoning**", ""]
                for c in g["common"]:
                    L.append(f"- ({c['n_runs']}/{g['n_runs']}) {c['representative']}")
                    rows.append((res["experiment"], s["slot"], g["group"], "shared", c["n_runs"], g["n_runs"],
                                 c["representative"]))
                L.append("")
            if g["varying"]:
                L += ["**Varying reasoning**", ""]
                for c in g["varying"][:max_varying]:
                    L.append(f"- ({c['n_runs']}/{g['n_runs']}) {c['representative']}")
                    rows.append((res["experiment"], s["slot"], g["group"], "varying", c["n_runs"], g["n_runs"],
                                 c["representative"]))
                if len(g["varying"]) > max_varying:
                    L.append(f"- … {len(g['varying']) - max_varying} more varying points")
                L.append("")
            if g["unique"]:
                L.append(f"Points made by a single run only: {g['unique']}.")
                L.append("")
            if g["phrases"]:
                L.append("Phrases used by at least half the runs: "
                         + ", ".join(f"“{p}” ({c})" for p, c in g["phrases"]) + ".")
                L.append("")
            if g["evidence"]:
                L.append("Evidence cited: " + ", ".join(f"{e} ({c})" for e, c in g["evidence"]) + ".")
                L.append("")
    out_md.write_text("\n".join(L), encoding="utf-8")
    if out_csv:
        import csv
        with out_csv.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["experiment", "slot", "group", "kind", "n_runs", "group_runs", "representative"])
            w.writerows(rows)
    return out_md
