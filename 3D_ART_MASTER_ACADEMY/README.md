# 3D Art Master Academy

Laboratorio di formazione personale: da principiante assoluto a modellatore, scultore e preparatore di stampa 3D autonomo, con Blender.

## Obiettivo reale: SH-Print

Azienda di stampa 3D artigianale: figure uniche e a tiratura limitata, non produzione di massa. Crescita futura con acquisizione di licenze dei marchi.

Regole su proprietà intellettuale:
- Gli esercizi possono usare personaggi famosi **solo per apprendimento privato**: non si vendono, non si pubblicano, non si mettono online (nemmeno su marketplace o social come "fan art in vendita").
- I file di allenamento con personaggi protetti restano in `PROGETTI/_STUDIO_PRIVATO/`.
- Le figure destinate alla vendita useranno personaggi originali oppure marchi **con licenza scritta**.
- Il corso include una parte su licenze, tirature limitate e documentazione del progetto. Non sono un consulente legale: per le licenze serve un avvocato esperto di proprietà intellettuale.

## Come funziona

1. Il tutor (Claude) prepara per ogni lezione una cartella in `LEZIONI/` con la dispensa.
2. Ogni lezione ha una **modalità guidata** (passo per passo) e una **autonoma** (solo consegna) in `02_esercitazione.md`.
3. Tu lavori in Blender e salvi i file nella cartella `consegne/` della lezione (mai sovrascrivere gli originali: usa `nome_v01.blend`, `nome_v02.blend`...).
4. Mi consegni il risultato (file `.blend`, render o screenshot). Lo correggo con voti 0–10 motivati.
5. Una competenza è segnata "acquisita" in `PROGRESSI.md` **solo dopo una prova pratica superata**, non dopo la lettura.

## Struttura

Ogni lezione ha **una sola cartella** in `LEZIONI/` con tutto il necessario:

```
LEZIONI/L01_interfaccia_e_navigazione/
  01_dispensa.md/.pdf        teoria, comandi, procedure, checklist
  02_esercitazione.md/.pdf   parte guidata + prova autonoma + criteri
  03_soluzioni.md       risposte di ripasso (da leggere dopo)
  materiali/            file di partenza e immagini di riferimento
  script/               script di generazione e di verifica
  consegne/             i TUOI file .blend e render di questa lezione
```

| Cartella | Contenuto |
|---|---|
| `LEZIONI/` | Una cartella per ogni lezione (vedi sopra). `_strumenti/crea_pdf.sh` converte i `.md` in PDF |
| `RIFERIMENTI/` | Immagini e tavole di riferimento (con licenza indicata) |
| `PROGETTI/` | Progetti integrati (`_STUDIO_PRIVATO/` per i personaggi protetti) |
| `FILE_BLEND/` | Tuoi file liberi, non legati a una lezione |
| `SCRIPT_BLENDER/` | Script generali riutilizzabili (analisi, esportazione) |
| `RENDER/` | Immagini finali e di verifica |
| `ANALISI_MODELLI/` | Report di analisi dei tuoi `.blend` |
| `STAMPA_3D/` | Modelli e verifiche per la stampa |
| `VERIFICHE/` | Prove di valutazione |
| `REPORT/` | Report generati |
| `BACKUP/` | Copie di sicurezza prima di ogni correzione automatica |

## Regole del laboratorio

- Nessun programma viene installato senza spiegazione e tua conferma.
- Nessun tuo file viene modificato: le correzioni vengono salvate come copia.
- Ciò che non posso verificare lo dichiaro come non verificato.

## File di controllo

- [`ROADMAP.md`](ROADMAP.md): percorso completo e stato.
- [`PROGRESSI.md`](PROGRESSI.md): registro lezioni, voti, competenze.
- [`GLOSSARIO.md`](GLOSSARIO.md): termini tecnici incontrati.

## Registro e schede stampabili

- `REGISTRO.md` / `REGISTRO.pdf`: registro delle attività per blocchi (date, esiti, voto finale), aggiornato dal tutor a ogni lezione.
- `LEZIONI/<cartella>/scheda_registro_LXX.pdf`: scheda stampabile della lezione (argomenti, esiti, voti) da ricopiare a mano.
- Per rigenerare: `python3 LEZIONI/_strumenti/genera_registro.py` e poi `crea_pdf.sh`.
