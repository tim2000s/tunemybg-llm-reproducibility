#!/bin/zsh
# Convert an analysis report.md to PDF: pandoc -> HTML (print CSS) -> headless Chrome.
# Usage: ./report_to_pdf.sh results/<experiment>/analysis/report.md [out.pdf]
set -e
md="$1"
out="${2:-${md%.md}.pdf}"
html="${md%.md}.html"
css="$(mktemp -t report-css).css"
cat > "$css" <<'EOF'
@page { size: A4 landscape; margin: 14mm; }
body { font-family: -apple-system, Helvetica, Arial, sans-serif; font-size: 10.5px; line-height: 1.35; color: #111; }
h1 { font-size: 20px; margin: 0 0 8px; } h2 { font-size: 15px; margin: 18px 0 6px; } h3 { font-size: 12.5px; margin: 14px 0 4px; }
code { font-family: Menlo, monospace; font-size: 9.5px; }
table { border-collapse: collapse; width: 100%; table-layout: auto; margin: 6px 0 10px; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #bbb; padding: 3px 5px; vertical-align: top; text-align: left;
         word-wrap: break-word; overflow-wrap: anywhere; font-size: 9px; }
th { background: #eee; }
li { margin: 1px 0; }
EOF
pandoc -s --metadata title=" " --css "$css" --embed-resources "$md" -o "$html"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --no-pdf-header-footer --print-to-pdf="$out" "file://$(cd "$(dirname "$html")" && pwd)/$(basename "$html")" 2>/dev/null
rm -f "$html" "$css"
echo "wrote $out"
