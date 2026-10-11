#!/usr/bin/env bash
# Converte uno o più file Markdown in PDF (A4) accanto al sorgente.
# Uso: LEZIONI/_strumenti/crea_pdf.sh LEZIONI/L01_.../01_dispensa.md [altri.md ...]
# Richiede: pandoc e Chromium (percorso in $CHROMIUM, default /opt/pw-browsers/chromium).
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
CHROME="${CHROMIUM:-$(command -v chromium || echo /opt/pw-browsers/chromium)}"
for md in "$@"; do
  [ -f "$md" ] || { echo "ERRORE: file non trovato: $md" >&2; exit 1; }
  base="${md%.md}"; html="$(mktemp --suffix=.html)"
  title="$(head -n1 "$md" | sed 's/^# *//')"
  pandoc "$md" -f gfm -t html5 -s --metadata title="$title" --metadata pagetitle="$title" \
    -V document-css=false --embed-resources -c "$DIR/stile_pdf.css" -o "$html" 2>/dev/null \
    || pandoc "$md" -f gfm -t html5 -s --metadata pagetitle="$title" --self-contained -c "$DIR/stile_pdf.css" -o "$html"
  # il titolo è già nel primo "# " del testo: evita doppioni
  sed -i '/<header id="title-block-header">/,/<\/header>/d' "$html"
  "$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$base.pdf" "file://$html" >/dev/null 2>&1
  rm -f "$html"
  [ -s "$base.pdf" ] && echo "OK  $base.pdf ($(du -h "$base.pdf" | cut -f1))" || { echo "ERRORE: PDF non creato per $md" >&2; exit 1; }
done
