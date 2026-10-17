#!/usr/bin/env bash
# Rigenera registro e schede, crea i PDF e copia REGISTRO.pdf in ogni cartella lezione.
# Uso (da 3D_ART_MASTER_ACADEMY):  bash LEZIONI/_strumenti/aggiorna_registro.sh
set -euo pipefail
python3 LEZIONI/_strumenti/genera_registro.py
bash LEZIONI/_strumenti/crea_pdf.sh REGISTRO.md LEZIONI/*/scheda_registro_*.md
for d in LEZIONI/L*/; do cp REGISTRO.pdf "${d}registro_attivita.pdf"; done
echo "Copiato REGISTRO.pdf in $(ls -d LEZIONI/L*/ | wc -l) cartelle."
