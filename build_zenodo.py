#!/usr/bin/env python3
"""Build the Zenodo preprint record files from the markdown sources in paper/.

Writes paper/zenodo/ with the study manuscript PDF (title page, abstract, body, references,
tables, figures), the supplementary tables as a separate PDF, the commentary PDF, the three figures as LZW TIFF and JPEG, and
the abstract as plain UTF-8 text for the record's description field. The PDFs are set in Times New
Roman, the font the set was first built in for medRxiv, which was abandoned on 8 September 2026
because its ethics declaration requires an institutional oversight body and this study has none.

Usage: python3 build_zenodo.py
"""
import pathlib
import re
import subprocess

import markdown
from weasyprint import CSS, HTML

PAPER = pathlib.Path(__file__).resolve().parent / "paper"
OUT = PAPER / "zenodo"
MAIN_MD = PAPER / "preprint_study_zenodo.md"
SUPP_MD = PAPER / "preprint_study_zenodo_supplement.md"
COMM_MD = PAPER / "preprint_commentary_zenodo.md"
FIGURES = [
    ("fig1_workflow.png", "Figure1"),
    ("fig2_suggested_values.png", "Figure2"),
    ("fig3_conversations.png", "Figure3"),
]

CSS_COMMON = """
body { font-family: 'Times New Roman', Times, serif; font-size: 11pt; line-height: 1.45;
       color: #000; }
h1 { font-size: 15pt; line-height: 1.3; margin: 0 0 5mm 0; font-weight: bold; }
h2 { font-size: 12pt; margin: 6mm 0 2mm 0; font-weight: bold; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 4mm 0 1.5mm 0; font-weight: bold; font-style: italic;
     page-break-after: avoid; }
p { margin: 0 0 2.8mm 0; text-align: left; }
a { color: #000; text-decoration: none; }
img { max-width: 100%; height: auto; display: block; margin: 4mm auto 2mm auto;
      page-break-inside: avoid; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 5mm 0; font-size: 8pt;
        line-height: 1.25; }
th { text-align: left; border-top: 1pt solid #000; border-bottom: 0.6pt solid #000;
     padding: 1mm 1.5mm; font-weight: bold; vertical-align: bottom; }
td { border-bottom: 0.3pt solid #999; padding: 0.9mm 1.5mm; vertical-align: top;
     overflow-wrap: anywhere; }
tr { page-break-inside: avoid; }
ol { padding-left: 5mm; }
li { margin: 0 0 1.2mm 0; }
"""

CSS_MAIN = CSS_COMMON + """
@page { size: A4 portrait; margin: 22mm 20mm 20mm 20mm;
        @bottom-center { content: counter(page); font: 9pt 'Times New Roman', serif; } }
"""

CSS_SUPP = CSS_COMMON + """
@page { size: A4 landscape; margin: 16mm 16mm 16mm 16mm;
        @bottom-center { content: counter(page); font: 9pt 'Times New Roman', serif; } }
table { font-size: 7.5pt; }
"""


def render(md_path: pathlib.Path, css: str, out_pdf: pathlib.Path) -> None:
    html = markdown.markdown(md_path.read_text(), extensions=["tables", "sane_lists"])
    # Short numeric cells (counts, n) wrap digit by digit in a narrow column; keep them whole.
    html = re.sub(r"<td>(\S{1,4})</td>", r'<td style="white-space:nowrap">\1</td>', html)
    doc = f"<html><head><meta charset='utf-8'></head><body>{html}</body></html>"
    HTML(string=doc, base_url=str(PAPER) + "/").write_pdf(out_pdf, stylesheets=[CSS(string=css)])
    print(f"wrote {out_pdf}")


STUDY_NOTE = ("Preprint, not peer reviewed. Under submission to the Journal of Diabetes Science and "
              "Technology. The companion commentary on the product's regulatory position is at "
              "https://doi.org/10.5281/zenodo.22662770. Code, prompts, every transcript and the study package with identifiers "
              "removed are at https://github.com/tim2000s/tunemybg-llm-reproducibility.")
COMMENTARY_NOTE = ("Preprint, not peer reviewed. Commentary under submission to the Journal of Diabetes "
                   "Science and Technology alongside the study it accompanies, which is a separate "
                   "Zenodo record. Not legal advice.")


def abstract_text(md_path: pathlib.Path, note: str) -> str:
    """The Abstract section as plain paragraphs, headed by the record note, for the description field."""
    text = md_path.read_text()
    m = re.search(r"^## Abstract\s*$(.*?)^## ", text, re.S | re.M)
    body = m.group(1).strip()
    paras = [re.sub(r"\s+", " ", p).strip() for p in body.split("\n\n") if p.strip()]
    return note + "\n\n" + "\n\n".join(paras) + "\n"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    render(MAIN_MD, CSS_MAIN, OUT / "TuneMyBG_preprint_manuscript.pdf")
    render(SUPP_MD, CSS_SUPP, OUT / "TuneMyBG_preprint_supplement.pdf")
    render(COMM_MD, CSS_MAIN, OUT / "TuneMyBG_commentary_manuscript.pdf")
    (OUT / "TuneMyBG_preprint_abstract.txt").write_text(abstract_text(MAIN_MD, STUDY_NOTE),
                                                        encoding="utf-8")
    (OUT / "TuneMyBG_commentary_abstract.txt").write_text(abstract_text(COMM_MD, COMMENTARY_NOTE),
                                                          encoding="utf-8")
    print(f"wrote {OUT / 'TuneMyBG_preprint_abstract.txt'} and TuneMyBG_commentary_abstract.txt")
    for src, stem in FIGURES:
        png = PAPER / "figures" / src
        # LZW keeps the TIFF near the PNG's size; uncompressed, the 900 dpi figures run to 95
        # to 138 MB each, over GitHub's file limit.
        for fmt, ext, opts in (("tiff", "tiff", ["-s", "formatOptions", "lzw"]),
                               ("jpeg", "jpg", ["-s", "formatOptions", "best"])):
            dst = OUT / f"{stem}.{ext}"
            subprocess.run(["sips", "-s", "format", fmt, *opts, str(png), "--out", str(dst)],
                           check=True, capture_output=True)
            print(f"wrote {dst}")


if __name__ == "__main__":
    main()
