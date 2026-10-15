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
| Mirror, Solidify e Array in sequenza guidata | L04 guidata 13/13 controlli (`L04_guidata_v02.blend`, caricato sulla radice di `main`) | 10/10 | ✅ acquisita |
| Correzione di uno stack di modificatori (ordine, scala, Merge) | L04 Parte C: 3/3 (`L04_stack_riparato_v02.blend`) | 10/10 | ✅ acquisita |
| Modellare in autonomia con Mirror + Solidify + Array | L04 Parte B: v02 11/13 su copia con nome corretto; v03 8/13 (Scale ≠ 1 usata per forzare le dimensioni); v04 12/13 su copia con nome corretto (soluzione valida con pareti verticali + Solidify, volume 8424 esatto); **v05 13/13** (`L04_autonoma_v05.blend`) | 8/10 | ✅ acquisita (v05 13/13) |
| Bevel (`Ctrl`+`B`) | L02 mini-prova: Tavolino con 12 spigoli del piano smussati, 2 segmenti, 5 mm; 10/10 controlli, mesh chiusa (`consegne_L02_bevel_v02.blend`) | 10/10 | ✅ acquisita |
| Subdivision Surface con supporti (Inset Individual) e Crease 0,5 | L05 guidata: `L05_guidata_v02.blend`, 11/12 controlli come consegnato; con il nome `Blocco_crease` corretto su una copia di prova sarebbe 13/13 (nome consegnato: `Blocco_Crease`) | 9/10 | ✅ acquisita |
| Riparazione di Subdivision (supporti, Crease, Shade Smooth) | L05 Parte C: 3/3 (`L05_blocchi_riparati_v02.blend`) | 10/10 | ✅ acquisita |
| Diagnosi scritta con frase causale (L05) | `Risposte.txt`: struttura «Poiché…, …, quindi…» corretta; Blocco_3 con conseguenza falsa ("in stampa non risulterà liscio") e meccanismi mancanti | 7/10 | 🟨 da consolidare |
| Subdivision autonoma: sapone con incavo | L05 Parte B: `L05_autonoma_v02.blend` 12/16 (outer edges senza supporti, incavo con pareti inclinate) | — | 🟨 da ripetere (v03) |

## Lezioni completate

| Data | Lezione | Modalità | Voto | Note |
|---|---|---|---|---|
| 2026-10-11 | L01 Interfaccia e navigazione | L01 completata: autonoma B e Parte C superate | 10/10 | Posizioni, scale e rotazioni esatte; versionamento v01-v03 corretto. Nota: il riferimento del Toro nella Parte C/guidata era sbagliato (tutor), corretto |
| 2026-10-13 | L02 Edit Mode e modellazione base | L02 completata: guidata, autonoma, riparazione e bevel superati | 9/10 | Quattro file perfetti. Punto perso solo nella diagnosi scritta (risposte 2, 4 e 6 imprecise) |
| 2026-10-14 | L03 Collezioni, gerarchie, unità, presentazione | L03 completata: guidata, autonoma e riparazione superate | 9/10 | Guidata 9, autonoma 10, riparazione 10, render 9. Punti persi: refuso `Caa_Tetto` e frase causale finale assente. Chiude la Fase 1 |
| 2026-10-14 | L04 Modificatori: Mirror, Solidify, Array | L04 completata: guidata 13/13, riparazione 3/3, autonoma superata alla v05 (13/13) | 8/10 | Parte B superata dopo tre revisioni (nome, scala forzata, quota Z). Frasi causali ancora con errori di contenuto (Vaschetta_3). Soluzione originale della cornice con pareti verticali |
| 2026-10-15 | L05 Subdivision Surface e spigoli | **In corso:** guidata 11/12 (nome), riparazione 3/3, autonoma 12/16 (da ripetere) | — | Voto finale dopo la Parte B |

## Difficoltà ricorrenti

- **Precisione nel descrivere i difetti di una mesh:** termini generici ("faccia esterna", "non lette in stampa") al posto di termini verificabili ("faccia frontale", "mesh non chiusa: lo slicer non distingue dentro e fuori"). Da esercitare nelle prossime lezioni scrivendo le risposte con termini della dispensa.
- **Spiegare il perché (causa → conseguenza):** per tre volte (L02 domanda 6, L03 frase finale, L04 Parte C punto 3) hai risposto con etichette o frasi circolari ("non stampabile perché errata") invece di spiegare il meccanismo. Esempio del formato richiesto: "Un modello non chiuso non si stampa perché lo slicer non distingue dentro e fuori". Da esercitare con una frase di spiegazione in ogni lezione. **Progresso (L04):** al quarto tentativo hai scritto frasi con struttura causale; restano errori di contenuto (Vaschetta_1 senza il meccanismo, Vaschetta_2 "dimensioni non corrette" mentre sono giuste, Vaschetta_3 con Merge che "raddoppia" i corpi, al contrario).
- **Nomi degli oggetti** (4 casi: `Caa_Tetto` in L03; `Vaschetta` e `Cube` al posto di `Cornice` in L04; `Blocco_Crease` al posto di `Blocco_crease` in L05: le maiuscole contano). I nomi esatti servono a controlli e script: rileggi la tabella dei requisiti prima di consegnare.
- **Correggere il sintomo invece della causa** (L04 Parte B, v03): per far tornare le dimensioni hai scalato l'oggetto (Scale 0.962, 0.953, 0.751) invece di correggere la geometria. Con la scala sbagliata lo spessore reale delle pareti cambia: va corretto a monte.
- **Frasi causali, contenuto (L05):** struttura corretta, ma Blocco_3: Flat/Smooth cambia solo il calcolo della luce, non la geometria stampata; e mancano il meccanismo (cosa fa il programma) e un numero misurabile (33,58 mm, volume 100%).
- **Controllare tutto il perimetro (L05 Parte B):** supporti messi sull'incavo ma non sui 12 spigoli esterni della scatola: il modello si restringe (78,75 × 48,75 × 19,76 mm).
