# Scheda di controllo L05 — Subdivision Surface (da stampare)

**Nome file di lavoro:** ______________________  **Data:** ____________  **Blender 5.0.1, comandi in inglese, 1 unità = 1 mm**

**Come si usa:** per ogni passo esegui l'azione, poi guarda la colonna **«Deve risultare»**. Se corrisponde, spunta ☐. Se **non** corrisponde, **fermati**: non andare avanti, rileggi il passo (dispensa/esercitazione) o scrivimi il numero del passo e cosa vedi.
Non modificare i file in `materiali/`. Salva con nomi versionati in `consegne/`. **Non applicare** Subdivision (Apply).

## PARTE A — Guidata (Blocco e Blocco_crease)

### A0. Preparazione
| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | Apri `materiali/L05_start.blend` | Scena con Camera, Sole, Pavimento |
| ☐ | `File → Save As` → `consegne/L05_guidata_v01.blend` | Titolo finestra = nuovo nome |
| ☐ | Outliner: collezioni | **Scena** (con 3 oggetti) e **Modello** (vuota) |

### A1. Il cubo «Blocco»
| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | Clic sulla collezione **Modello** | Evidenziata: è la collezione attiva |
| ☐ | Mouse sulla viewport, `Shift`+`C` | 3D Cursor al centro |
| ☐ | `Add → Mesh → Cube` | Un cubo, nell'Outliner **dentro Modello** |
| ☐ | `N` → Item → **Dimensions** `40`, `40`, `40` | Tre valori 40 mm |
| ☐ | `Ctrl`+`A` → **Scale** | **Scale = 1, 1, 1**, Dimensions ancora 40 |
| ☐ | **Location** `0`, `0`, `20` | Il cubo poggia sul pavimento |
| ☐ | `F2` → nome **Blocco** (B maiuscola) | Nome esatto nell'Outliner |

### A2. Subdivision (a mano)
| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | Properties → **Modifiers** → `Add Modifier → Generate → Subdivision Surface` | Il modificatore compare nel pannello |
| ☐ | **Levels Viewport** = `2` | Forma simile a una sfera |
| ☐ | **Render** = `3` | Campo Render = 3 |

### A3. Misura SENZA supporti (sulla copia)
| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | `Shift`+`D`, clic destro | Copia sopra l'originale |
| ☐ | Sulla copia: menu del modificatore → **Apply** | Il modificatore sparisce dalla copia |
| ☐ | Overlays → **Statistics** (acceso) | Visibile conteggio |
| ☐ | Leggi Statistics e `N` → Dimensions della copia | **98 vertici, 96 facce**; dimensioni **≈ 33,58 mm** per asse |
| ☐ | Scrivi qui i tuoi valori: vertici ______ facce ______ dim. ______ | Servono per la frase finale |
| ☐ | Elimina la copia (`X` → Delete) | Rimane solo **Blocco** (verifica: Outliner) |

### A4. Supporti (Inset individuale)
| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | Seleziona **Blocco**, `Tab`, modo **Face** (tasto `3`), `A` | Tutte le facce selezionate |
| ☐ | `I`, digita `4`, `Enter` | (all'inizio sembra non succedere nulla) |
| ☐ | Pannello **Inset Faces** (in basso a sinistra): spunta **Individual** | Ogni faccia ha una cornice interna |
| ☐ | Statistics in Edit Mode | **32 vertici, 60 spigoli, 30 facce** |
| ☐ | `Tab` | Object Mode: il blocco ha spigoli smussati |

### A5. Misura CON supporti (sulla copia)
| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | `Shift`+`D`, clic destro, **Apply** sulla copia | |
| ☐ | Dimensions della copia | **40 × 40 × 40 mm** |
| ☐ | Statistics della copia | **482 vertici, 480 facce** |
| ☐ | Elimina la copia | Resta solo **Blocco** |

### A6. Prova facoltativa (2 mm e 6 mm)
| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | Facoltativo: in Edit Mode annulla l'Inset e prova `2` poi `6` | Con 2 mm gli spigoli sono più netti, con 6 più morbidi |
| ☐ | **Riporta a 4 mm** prima di consegnare | Statistics Edit Mode: 32 / 60 / 30 |

### A7. Shade Smooth
| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | Object Mode, **Blocco** selezionato: menu **Object → Shade Smooth** | Niente sfaccettature visibili |

### A8. «Blocco_crease»
| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | Collezione **Modello** attiva, `Shift`+`C`, `Add → Mesh → Cube` | Nuovo cubo dentro Modello |
| ☐ | Dimensions `40`,`40`,`40`; `Ctrl`+`A` → **Scale** | Scale 1 |
| ☐ | Location `70`, `0`, `20`; nome **Blocco_crease** | Nome esatto |
| ☐ | `Add Modifier → Subdivision Surface`: Viewport `2`, Render `3` | |
| ☐ | `Tab`, modo **Edge** (tasto `2`), `A` | 12 spigoli selezionati |
| ☐ | `Shift`+`E`, digita `0.5`, `Enter` | Spigoli colorati (overlay **Crease** acceso) |
| ☐ | `Tab`, **Object → Shade Smooth** | Forma simile a Blocco, base di **8 vertici** |

### A9. Requisiti prima di caricare — PARTE A
| ☐ | Requisito |
|---|---|
| ☐ | Nomi esatti: **Blocco** e **Blocco_crease** |
| ☐ | Entrambi in **Modello**, nessun oggetto nella radice della scena (Outliner) |
| ☐ | **Scale 1,1,1** e rotazione 0 su entrambi (`N`) |
| ☐ | Un solo modificatore Subdivision per oggetto: **Viewport 2, Render 3**, NON applicato |
| ☐ | Blocco: 32 vertici nella base; Blocco_crease: 8 vertici, crease 0,5 |
| ☐ | Shade Smooth su entrambi |
| ☐ | Nessuna copia rimasta nella scena (solo Camera, Sole, Pavimento, Blocco, Blocco_crease) |
| ☐ | Salvato come `consegne/L05_guidata_v02.blend` (e caricato nel repository) |

<div style="page-break-after: always"></div>

## PARTE B — Autonoma: il Sapone

File: `consegne/L05_autonoma_v01.blend` (parti da `L05_start.blend`). **Non ti do i passaggi**: usa questa scheda per controllarti.

### B1. Controlli DURANTE il lavoro
| ☐ | Controllo | Come lo verifichi |
|---|---|---|
| ☐ | Cubo base creato, **Dimensions 80 × 50 × 20** e **Apply Scale** fatto | `N`: Scale 1,1,1 |
| ☐ | Origine nel centro, **Location 0, 0, 10** | `N` → Location; il sapone poggia sul pavimento |
| ☐ | Supporti sugli spigoli esterni | In Edit Mode: anelli di spigoli vicini ai bordi (2–6 mm) |
| ☐ | Incavo: pareti a **X ±25** e **Y ±10** | Clic su un vertice del bordo: `N` → Vertex (in Global) |
| ☐ | Incavo profondo **1,5 mm** (fondo a Z = 18,5) | Vertice del fondo: Z (Global) = 18.5 |
| ☐ | Anello di supporto **vicino al bordo dell'incavo** e **sul fondo** | Vedi disegno sotto |
| ☐ | Solo **quad** (nessun triangolo/n-gon) | Guarda la base in Edit Mode: nessuna faccia con 3 o 5+ lati |
| ☐ | Subdivision **Viewport 2, Render 3** | Pannello Modifiers |
| ☐ | **Shade Smooth** | Object → Shade Smooth |

**Disegna qui lo schema dei supporti dell'incavo (vista dall'alto) prima di costruirlo:**

<div style="border:1px solid #888; height:90mm; margin-bottom:6mm"></div>

### B2. Misura sulla copia
| ☐ | Controllo | Deve risultare |
|---|---|---|
| ☐ | `Shift`+`D` → **Apply** sulla copia → Dimensions | **80 × 50 × 20 mm** (i supporti tengono le facce piatte) |
| ☐ | Forma a occhio | Spigoli arrotondati (non gonfia, non a spigolo vivo) |
| ☐ | Bordo dell'incavo | Netto, non sfumato; fondo piatto |
| ☐ | Elimina la copia | Nessun oggetto extra |

### B3. Requisiti prima di caricare — PARTE B (tutti)
| ☐ | # | Requisito |
|---|---|---|
| ☐ | 1 | Oggetto **Sapone** (nome esatto), collezione **Modello**, nulla fuori dalle collezioni |
| ☐ | 2 | Scale **1**, rotazione 0 |
| ☐ | 3 | Un solo modificatore **Subdivision**, **Viewport 2, Render 3**, non applicato |
| ☐ | 4 | Base **solo quad** |
| ☐ | 5 | Base 80 × 50 × 20, **centrata** su X e Y, **Z da 0 a 20** |
| ☐ | 6 | Incavo: pareti **X ±25, Y ±10**, **profondità 1,5**, fondo a Z = 18,5 |
| ☐ | 7 | Dimensioni finali **80 × 50 × 20** |
| ☐ | 8 | Spigoli arrotondati nella misura giusta (né gonfio né vivo) |
| ☐ | 9 | Fondo dell'incavo a Z = 18,5 |
| ☐ | 10 | Bordo dell'incavo netto (supporti vicini) |
| ☐ | 11 | **Shade Smooth** su tutte le facce |
| ☐ | 12 | Chiuso, **1 corpo**, nessun vertice doppio (nessuna copia rimasta nella scena) |
| ☐ | 13 | Unità in mm |
| ☐ | — | Salvato `consegne/L05_autonoma_v01.blend` (o v02, v03…) e caricato |

<div style="page-break-after: always"></div>

## PARTE C — Diagnosi e riparazione dei tre blocchi

File: `materiali/L05_blocchi_sbagliati.blend` → salva come `consegne/L05_blocchi_riparati_v01.blend`.

### C1. Indagine (compila prima di riparare)
Per ognuno: misura sulla copia con Apply (dimensioni, Statistics), guarda overlay **Crease** (Edit Mode, Edge) e l'aspetto della superficie.

| Oggetto | Statistics base (V/F) | Dimensioni sulla copia | Crease visibile? | Superficie sfaccettata? |
|---|---|---|---|---|
| Blocco_1 | ______ / ______ | ______ | ☐ sì ☐ no | ☐ sì ☐ no |
| Blocco_2 | ______ / ______ | ______ | ☐ sì ☐ no | ☐ sì ☐ no |
| Blocco_3 | ______ / ______ | ______ | ☐ sì ☐ no | ☐ sì ☐ no |

### C2. Diagnosi scritta (4 punti per ogni oggetto)
Formato della frase: **«Poiché [cosa succede nel programma], [effetto], quindi [conseguenza misurabile]»**.

**Blocco_1**
1. Difetto: ______________________________________________
2. Come l'ho riconosciuto (numero o immagine): ______________________________________________
3. Frase causale: ____________________________________________________________________________________________________________________________________
4. Correzione: ______________________________________________

**Blocco_2**
1. Difetto: ______________________________________________
2. Come l'ho riconosciuto: ______________________________________________
3. Frase causale: ____________________________________________________________________________________________________________________________________
4. Correzione: ______________________________________________

**Blocco_3**
1. Difetto: ______________________________________________
2. Come l'ho riconosciuto: ______________________________________________
3. Frase causale: ____________________________________________________________________________________________________________________________________
4. Correzione: ______________________________________________

### C3. Riparazione — controlli
| ☐ | Controllo | Deve risultare |
|---|---|---|
| ☐ | Blocco_1: supporti aggiunti (o crease) | Dimensioni sulla copia **40 mm** |
| ☐ | Blocco_2: crease ridotto/azzerato (`Shift`+`E` con `-1` o `0.5`) | Spigoli arrotondati, non vivi |
| ☐ | Blocco_3: **Object → Shade Smooth** | Nessuna sfaccettatura |
| ☐ | Tutti e tre: **Subdivision livello 2**, non applicato | Un solo modificatore ciascuno |
| ☐ | Scale 1, **nomi e posizioni invariati** (X −70 / 0 / +70, Z 20) | Controlla `N` |
| ☐ | Base solo quad, nessuna copia rimasta | Outliner pulito |
| ☐ | Salvato `consegne/L05_blocchi_riparati_v01.blend` e caricato | |

<div style="page-break-after: always"></div>

## Se qualcosa non torna (guida rapida)

| Sintomo | Causa probabile | Cosa fare |
|---|---|---|
| Il blocco è una palla piccola (33,6 mm) | Nessun supporto | Fai l'Inset **Individual** (A4) |
| `I` non fa nulla su tutte le facce | **Individual** spento | Spuntalo nel pannello Inset Faces |
| Dopo Apply vedo migliaia di facce nell'originale | Hai applicato il modificatore sull'originale | `Ctrl`+`Z` oppure riparti dall'ultimo salvataggio |
| Dimensions diversi da quelli attesi | Scala non applicata | `Ctrl`+`A` → Scale, poi ricontrolla |
| Superficie a «gradini» | Flat Shading | Object → Shade Smooth |
| Il bordo dell'incavo è sfumato | Mancano supporti vicino al bordo/fondo | Aggiungi un anello a circa 1,5 mm |
| Statistics non compare | Overlay spento | Overlays → Statistics |
| `Ctrl`+`2` non funziona | Scorciatoia non attiva sul tuo PC | Usa Add Modifier (già previsto) |

## Firma finale
Ho spuntato **tutte** le caselle prima di caricare: ☐  Data: ____________  Versione caricata: ____________
