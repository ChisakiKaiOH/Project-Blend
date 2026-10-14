# Registro dei progressi

## Competenze

| Competenza | Prova pratica | Voto | Stato |
|---|---|---|---|
| Navigazione viewport, selezione, Location e Scale con valori precisi (Object Mode) | L01 autonoma B: 5/5 con script (file `L01_autonoma_v02.blend`) | 10/10 | ✅ acquisita |
| Rotazione (`R`, assi, valori) e appoggio al pavimento | L01 Parte C: 5/5 con script (file `L01_autonoma_v03.blend`) | 10/10 | ✅ acquisita |
| Edit Mode, selezione, Loop Cut, Extrude, Inset con valori numerici, Apply Scale | L02 guidata 10/10 (`L02_guidata_v02.blend`) e autonoma 10/10 (`L02_autonoma_v02.blend`) | 10/10 | ✅ acquisita |
| Riparazione di mesh (buco, vertici sciolti, normali) | L02 Parte C: 6/6 con script (`L02_riparata_v01.blend`) | 10/10 | ✅ acquisita |
| Diagnosi scritta di una mesh difettosa | L02 Parte C, risposte scritte | 7/10 | 🟨 da consolidare (terminologia e causa principale) |
| Unità in mm, collezioni, gerarchie con Keep Transform, nomi, immagine di riferimento | L03 guidata 17/18 controlli (un refuso nel nome `Caa_Tetto`) e autonoma 22/22 (`L03_guidata_v02.blend`, `L03_autonoma_v02.blend`) | 9/10 e 10/10 | ✅ acquisita |
| Render semplice in Eevee e salvataggio del PNG | L03 `L03_casetta_render_v01.png` 1600×900, casa intera, con ombre | 9/10 | ✅ acquisita |
| Riparazione: normali invertite e faccia interna | L03 Parte C: Oggetto_A e Oggetto_B corretti (`L03_diagnosi_riparata_v02.blend`) | — | ✅ acquisita |
| Riparazione: vertici doppi (`M` → By Distance) | L03 Parte C: tutti e tre gli oggetti riparati, 3/3 (`L03_diagnosi_riparata_v03.blend`) | 10/10 | ✅ acquisita |
| Bevel (`Ctrl`+`B`) | L02 mini-prova: Tavolino con 12 spigoli del piano smussati, 2 segmenti, 5 mm; 10/10 controlli, mesh chiusa (`consegne_L02_bevel_v02.blend`) | 10/10 | ✅ acquisita |

## Lezioni completate

| Data | Lezione | Modalità | Voto | Note |
|---|---|---|---|---|
| 2026-10-11 | L01 Interfaccia e navigazione | L01 completata: autonoma B e Parte C superate | 10/10 | Posizioni, scale e rotazioni esatte; versionamento v01-v03 corretto. Nota: il riferimento del Toro nella Parte C/guidata era sbagliato (tutor), corretto |
| 2026-10-13 | L02 Edit Mode e modellazione base | L02 completata: guidata, autonoma, riparazione e bevel superati | 9/10 | Quattro file perfetti. Punto perso solo nella diagnosi scritta (risposte 2, 4 e 6 imprecise) |
| 2026-10-14 | L03 Collezioni, gerarchie, unità, presentazione | L03 completata: guidata, autonoma e riparazione superate | 9/10 | Guidata 9, autonoma 10, riparazione 10, render 9. Punti persi: refuso `Caa_Tetto` e frase causale finale assente. Chiude la Fase 1 |

## Difficoltà ricorrenti

- **Precisione nel descrivere i difetti di una mesh:** termini generici ("faccia esterna", "non lette in stampa") al posto di termini verificabili ("faccia frontale", "mesh non chiusa: lo slicer non distingue dentro e fuori"). Da esercitare nelle prossime lezioni scrivendo le risposte con termini della dispensa.
- **Spiegare il perché (causa → conseguenza):** per due volte (L02 domanda 6, L03 frase finale) hai elencato etichette senza spiegare perché una mesh difettosa non si stampa. Esempio del formato richiesto: "Un modello non chiuso non si stampa perché lo slicer non distingue dentro e fuori". Da esercitare con una frase di spiegazione in ogni lezione.
- **Attenzione ai refusi nei nomi** (1 caso: `Caa_Tetto`). I nomi esatti servono a controlli e script: rileggili prima di consegnare.
