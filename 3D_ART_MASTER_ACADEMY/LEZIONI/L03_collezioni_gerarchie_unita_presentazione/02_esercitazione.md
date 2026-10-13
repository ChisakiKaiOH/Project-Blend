# Esercitazione L03 — La casetta, la scena da riordinare e la diagnosi

**Livello:** 2–3 · **Tempo indicativo:** guidata 75–90 min, autonoma 30–40 min, diagnosi e riparazione 25–30 min
**Strumenti:** Blender 5.0.1, file in `materiali/`
**Dispensa:** `01_dispensa.md`

Salva sempre con nomi versionati (`_v01`, `_v02`, …) nella cartella `consegne/` di questa lezione. **Non modificare i file in `materiali/`.** Le unità dei file didattici sono pensate in millimetri: **1 unità Blender = 1 mm**.

---

## Parte A — Modalità guidata: la casetta

**Obiettivo:** costruire una casetta in millimetri, con parti in gerarchia, collezioni ordinate, un'immagine di riferimento e un render finale. Riferimento visivo: `materiali/L03_riferimento_casetta.png`.

### A0. Preparazione
1. Apri `materiali/L03_start.blend` e salvalo subito come `consegne/L03_guidata_v01.blend`.
2. La scena contiene **Camera**, **Sole** e **Pavimento** (200 × 200 mm) direttamente nella Scene Collection.

### A1. Imposta le unità
1. Properties editor → scheda **Scene** → pannello **Units**.
2. **Unit System:** Metric · **Unit Scale:** `0.001` · **Length:** Millimeters.
3. **Verifica:** clicca il Pavimento, premi `N` → Item: **Dimensions** devono mostrare `200 mm`.

### A2. Crea le collezioni
1. Nell'Outliner: clic destro → **New Collection**, ripeti per ottenere tre collezioni. Rinominale (`F2`): **Scena**, **Casa**, **Riferimenti**.
2. Seleziona **Camera**, **Sole** e **Pavimento** (clic e `Ctrl` + clic nell'Outliner), mouse sulla viewport, `M` → **Scena**.
3. **Verifica:** nell'Outliner sotto Scene Collection vedi Scena (con i tre oggetti), Casa e Riferimenti (vuote). Nessun oggetto fuori.

### A3. Il root della casa
1. Clic sulla collezione **Casa** nell'Outliner (diventa la collezione attiva).
2. `Shift` + `C` riporta il 3D Cursor al centro. Menu `Add → Empty → Plain Axes`.
3. Rinominalo **Casa_ROOT**. In `N` → Item controlla **Location** = 0, 0, 0.

### A4. Il corpo
1. `Add → Mesh → Cube`. In `N`: **Dimensions** `60`, `40`, `40`. Poi `Ctrl` + `A` → **Scale** (Apply Scale).
2. **Location:** `0`, `0`, `20`. Rinomina **Casa_Corpo**.
3. **Verifica:** Scale = 1, 1, 1; Dimensions = 60 × 40 × 40 mm.

### A5. Il tetto a capanna
1. `Add → Mesh → Cube`. Dimensions `66`, `46`, `10`. Apply Scale. **Location** `0`, `0`, `45`. Rinomina **Casa_Tetto**.
2. `Tab` (Edit Mode). Overlays → Statistics acceso: 8 vertici, 12 spigoli, 6 facce.
3. `Ctrl` + `R`: porta il mouse su uno degli spigoli **corti** (quelli lungo Y), finché l'anello giallo gira intorno al piano **lungo la direzione X**; **1 taglio**, clic sinistro, poi clic destro (taglio al centro).
4. **Risultato atteso:** 12 vertici, 20 spigoli, 10 facce.
5. Modo **Edge**. Seleziona lo spigolo nuovo **in alto al centro** (quello che corre lungo X).
6. `G`, `Z`, `10`, `Enter`: il colmo sale di 10 mm.
7. `Tab`. **Risultato atteso:** Dimensions 66 × 46 × 20 mm, la base del tetto a Z = 40, il colmo a Z = 60.

### A6. La porta
`Add → Mesh → Cube`. Dimensions `12`, `2`, `22`. Apply Scale. **Location** `0`, `-20`, `11`. Rinomina **Casa_Porta**.

### A7. Il camino
`Add → Mesh → Cube`. Dimensions `8`, `8`, `20`. Apply Scale. **Location** `-20`, `10`, `58`. Rinomina **Casa_Camino**.

### A8. La gerarchia
1. Nell'Outliner seleziona le 4 parti (`Ctrl` + clic), poi `Ctrl` + clic su **Casa_ROOT** per ultimo (deve essere l'oggetto attivo).
2. Mouse sulla viewport: `Ctrl` + `P` → **Object (Keep Transform)**.
3. **Verifica:** nell'Outliner le 4 parti sono indentate sotto Casa_ROOT.
4. **Prova:** seleziona Casa_ROOT, `G`, `X`, `30`, `Enter`: tutta la casa si sposta. Poi `Ctrl` + `Z` (la Location di Casa_ROOT deve tornare 0, 0, 0).

### A9. L'immagine di riferimento
1. Clic sulla collezione **Riferimenti**.
2. `Add → Image → Reference` → scegli `materiali/L03_riferimento_casetta.png`.
3. Spostala di lato (es. X = `-150`) e rinominala **Rif_Casetta**.
4. **Verifica:** nell'Outliner Rif_Casetta è dentro Riferimenti.

### A10. La camera e il render
1. Gira la vista finché vedi la casa intera con il camino.
2. `View → Align View → Align Active Camera to View`.
3. Render Properties: **Render Engine** = EEVEE. Output Properties: **Resolution** 1600 × 900, 100%.
4. `View → Viewpoint → Camera`, controlla che la casa sia inquadrata per intero.
5. `F12`. Nella finestra Render Result: `Image → Save As` → PNG → `consegne/L03_casetta_render_v01.png`.
6. Chiudi la finestra del render. Salva come `consegne/L03_guidata_v02.blend`.

### A11. Controllo
Carica il `.blend` e il PNG e scrivimi "consegna guidata L03": lo controllo con `script/verifica_L03.py -- A`.

---

## Parte B — Modalità autonoma: riordina la scena (prova di superamento)

**Consegna:** apri `materiali/L03_scena_disordinata.blend` e salvalo come `consegne/L03_autonoma_v01.blend`. La scena contiene un piccolo giardino fatto di forme semplici con nomi di default (`Cube`, `Cylinder.001`, `Cone`…) e tutto fuori dalle collezioni. **Non devi spostare né eliminare nessun oggetto.**

**Requisiti (tutti misurati dallo script):**

| # | Requisito |
|---|---|
| 1 | Unità: **Metric**, Unit Scale **0.001**, Length **Millimeters** |
| 2 | Quattro collezioni con questi nomi esatti: **Albero**, **Lampione**, **Panchina**, **Scena** |
| 3 | Individua tu **quali oggetti formano un gruppo** guardando dove si trovano (vista Top) e mettili nella collezione del gruppo (il gruppo "Albero" è l'albero, ecc.) |
| 4 | In **Scena**: camera, luce e pavimento |
| 5 | Per ogni gruppo un Empty chiamato **<Gruppo>_ROOT** (es. `Albero_ROOT`) nella collezione del gruppo, **a terra (Z = 0), al centro del gruppo** (tolleranza 2 mm), senza genitore |
| 6 | Tutte le parti del gruppo sono **figlie** del suo ROOT (Keep Transform) |
| 7 | Nomi delle parti con il prefisso del gruppo e un trattino basso, per esempio `Albero_Tronco`; **nessun nome di default** (anche il pavimento: non deve più chiamarsi `Plane`) |
| 8 | Le posizioni delle parti **non sono cambiate** |
| 9 | Nessun oggetto fuori dalle collezioni |

**Non ti do i passaggi.** Se ti blocchi:
- per vedere dove si trova un oggetto: clic, `N` → Item → Location; o vista dall'alto (`View → Viewpoint → Top`);
- il "centro del gruppo" è il centro dello spazio occupato dalle sue parti (pensa al punto di appoggio).

**Consegna:** carica `consegne/L03_autonoma_v01.blend` (e le versioni successive) e scrivimi "consegna L03".

### Criteri di superamento
| Criterio | Come lo verifico |
|---|---|
| Requisiti 1–9 | `script/verifica_L03.py -- B` |
| Salvataggio versionato | Nomi dei file nel repository |

**Condizione per superarla:** **22/22 controlli** dello script.

---

## Parte C — Diagnosi e riparazione di tre mesh

**Consegna:** apri `materiali/L03_mesh_diagnosi.blend` e salvalo come `consegne/L03_diagnosi_riparata_v01.blend`. La scena contiene tre cubi di 20 mm, **Oggetto_A**, **Oggetto_B** e **Oggetto_C**, ognuno con un **difetto diverso**.

**Diagnosi:** per **ciascun** oggetto scrivimi (prima di riparare):
1. i numeri di Statistics (vertici, spigoli, facce) con niente selezionato;
2. cosa selezionano `Select → Select All by Trait → Non Manifold` e `Interior Faces` (quanti spigoli o facce);
3. il colore che mostra **Face Orientation**;
4. il **nome del difetto**, scelto tra questi termini della dispensa: *normali invertite, mesh non chiusa (non-manifold), spigoli di bordo, faccia interna, vertici doppi, corpo (shell)*.

In **una frase** scrivi poi perché nessuno dei tre si stampa correttamente. Usa i termini sopra, non parole generiche come "esterna" o "non letto".

**Riparazione:** porta tutti e tre a mesh chiuse, un solo corpo, normali verso l'esterno, nessun vertice doppio, nomi invariati, senza modificatori.

**Consegna:** carica `consegne/L03_diagnosi_riparata_v01.blend` e scrivimi "consegna diagnosi L03". Controllo con `script/verifica_L03_C.py`.

**Condizione per superarla:** 3/3 controlli dello script **e** diagnosi scritta con i termini corretti.

---

## Errori da evitare
- Lavorare sui file in `materiali/`.
- Cambiare le unità a scena già costruita.
- `Ctrl` + `P` senza Keep Transform.
- Lasciare oggetti fuori dalle collezioni o con nomi di default.
- Scrivere le risposte con parole generiche invece dei termini tecnici.

### Difficoltà
⭐⭐⭐ (tre stelle su cinque)
