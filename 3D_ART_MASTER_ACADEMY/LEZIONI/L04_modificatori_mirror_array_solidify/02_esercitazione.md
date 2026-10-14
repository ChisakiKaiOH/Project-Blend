# Esercitazione L04 — Vaschetta, cornice e stack sbagliati

**Livello:** 3 · **Tempo indicativo:** guidata 60–75 min, autonoma 40–50 min, riparazione 30 min
**Strumenti:** Blender 5.0.1, file in `materiali/`
**Dispensa:** `01_dispensa.md`

Salva sempre con nomi versionati (`_v01`, `_v02`, …) in `consegne/`. **Non modificare i file in `materiali/`.** Unità: **1 unità Blender = 1 mm**. In questa lezione **non applichi** i modificatori: li lasci attivi.

---

## Parte A — Modalità guidata: tre vaschette

**Obiettivo:** una vaschetta 80 × 50 × 20 mm con pareti da 2 mm, modellata **a metà**, ripetuta 3 volte con un vuoto di 10 mm. Riferimento: `materiali/L04_riferimento_A.png`.

### A0. Preparazione
1. Apri `materiali/L04_start.blend` e salvalo come `consegne/L04_guidata_v01.blend`.
2. La scena ha già le unità in millimetri e due collezioni: **Scena** (Camera, Sole, Pavimento) e **Modello** (vuota).

### A1. Il cubo di partenza
1. Clic sulla collezione **Modello** (diventa la collezione attiva).
2. `Shift` + `C` (3D Cursor al centro, di default a 0,0,0).
3. `Add → Mesh → Cube`. In `N` → Item: **Dimensions** `40`, `50`, `20`. `Ctrl` + `A` → **Scale**.
4. **Location** `-20`, `0`, `10`. Rinomina **Vaschetta** (`F2`).
5. **Verifica:** Scale = 1, Dimensions = 40 × 50 × 20 mm. Il cubo occupa X da -40 a 0.

### A2. L'origine sul piano di specchio
1. Il 3D Cursor è al centro. Menu `Object → Set Origin → Origin to 3D Cursor`.
2. **Verifica:** in `N` la **Location** è ora `0`, `0`, `0` e il cubo non si è mosso.

### A3. Elimina le facce sul piano di specchio e in alto
1. `Tab`, modo **Face**, vista da destra: `View → Viewpoint → Right`.
2. Clic sulla faccia che si trova a X = 0 (quella rivolta al centro della scena). Poi `View → Viewpoint → Top` e `Shift` + clic sulla faccia superiore.
3. Overlays → Statistics: **Faces 2/6**.
4. `X` → **Faces** (non *Only Faces*: vedi dispensa 4.1).
5. **Risultato atteso:** **8 vertici, 11 spigoli, 4 facce**.
6. `Tab` per tornare in Object Mode.

### A4. Mirror
1. Properties → scheda **Modifiers** → `Add Modifier → Generate → Mirror`.
2. Controlla: asse **X** acceso, **Merge Vertices** acceso.
3. **Verifica:** la vaschetta è intera, senza pareti spesse. In `N` → Dimensions: **80 × 50 × 20 mm**.

### A5. Solidify
1. `Add Modifier → Generate → Solidify`.
2. **Thickness** `2`. **Offset** `-1` (valore predefinito). Attiva **Even Thickness**. **Fill Rim** acceso.
3. **Verifica:** Dimensions restano **80 × 50 × 20 mm**; guardando dall'alto vedi pareti da 2 mm.

### A6. Prova dell'ordine (esperimento)
1. Nel pannello **Solidify**, menu a discesa → **Move to First** (Solidify sopra Mirror).
2. Controlla il risultato **su una copia** (dispensa 7.1): `Shift` + `D` e clic destro; sul duplicato applica i modificatori dall'alto verso il basso; Edit Mode, modo Edge, `Select → Select All by Trait → Non Manifold`.
3. **Risultato atteso:** **8 spigoli non-manifold** (la copia ha 24 vertici, 46 spigoli, 25 facce). Annota una frase su ciò che hai capito. Poi elimina il duplicato.
4. Rimetti l'ordine corretto sull'originale: menu a discesa di Solidify → **Move to Last**. Lo stack deve essere **Mirror, Solidify**.

### A7. Array
1. `Add Modifier → Generate → Array` (la prima voce).
2. **Count** `3`. **Offset Method** Relative. **Offset X** `1.125` (Y e Z restano 0).
3. **Perché 1.125?** La vaschetta è larga 80 mm e il vuoto è 10 mm: (80 + 10) / 80 = 1.125.
4. **Verifica:** Dimensions = **260 × 50 × 20 mm** (3 × 80 + 2 × 10); tre vaschette separate.
5. *Alternativa con Array (Legacy):* Count `3`, Relative Offset spento, Constant Offset acceso con X = `90`.
6. **Lo stack finale deve essere: Mirror → Solidify → Array.**

### A8. Controllo e consegna
1. `Overlays → Face Orientation`: tutto **blu**. Poi disattivala.
2. Salva come `consegne/L04_guidata_v02.blend`.
3. Carica il file e scrivimi "consegna guidata L04". Lo controllo con `script/verifica_L04.py -- A`.

---

## Parte B — Modalità autonoma: la cornice (prova di superamento)

**Consegna:** apri di nuovo `materiali/L04_start.blend`, salvalo come `consegne/L04_autonoma_v01.blend` e costruisci una **cornice** rettangolare, **3 copie** in fila, usando **Mirror, Solidify e Array**. Riferimento: `materiali/L04_riferimento_B.png`.

**Requisiti (tutti misurati dallo script sulla mesh dopo i modificatori):**

| # | Requisito |
|---|---|
| 1 | Oggetto chiamato **Cornice**, nella collezione **Modello**, nessun oggetto fuori dalle collezioni |
| 2 | **Scale = 1**, rotazione 0 (Apply fatto prima dei modificatori) |
| 3 | Stack dei modificatori: **Mirror → Solidify → Array** (non applicati, tutti attivi) |
| 4 | Mesh di partenza = **metà** della cornice (X da -25 a 0); Mirror su X con **Merge Vertices** |
| 5 | Ogni cornice: **50 × 40 mm** all'esterno, **barre larghe 6 mm** (foro 38 × 28 mm) |
| 6 | Spessore **3 mm**, la cornice poggia sul piano: **Z da 0 a 3 mm** |
| 7 | **3 copie** in fila lungo X con un **vuoto di 10 mm** tra l'una e l'altra: dimensioni finali **170 × 40 × 3 mm** |
| 8 | Mesh finale **chiusa**, **3 corpi** separati, nessun vertice doppio, volume **8424 mm³** (±1,5%) |
| 9 | Unità in mm |

**Non ti do i passaggi.** Pensa a come si presenta una cornice dimezzata (una forma a "C") e a come arrivarci con gli strumenti della Lezione 2.

**Aiuti (leggili solo se ti blocchi):**
- Il piano base è una lastra sul piano XY, con le normali verso l'alto. Per ottenere la forma a "C" ti servono tagli (Loop Cut) a distanza precisa dal bordo e la cancellazione della faccia interna con `X` → **Faces**.
- Con la lastra a Z = 0 e le normali verso l'alto, in quale verso deve crescere lo spessore? Guarda l'Offset di Solidify.
- L'Offset dell'Array è **relativo** alla larghezza della cornice: usa la formula (L + G) / L della dispensa.
- Per verificare il volume di una cornice: area × spessore, con area = esterno − foro.

**Consegna:** carica `consegne/L04_autonoma_v01.blend` (e le versioni successive) e scrivimi "consegna L04".

### Criteri di superamento

| Criterio | Come lo verifico |
|---|---|
| Requisiti 1–9 | `script/verifica_L04.py -- B` |
| Salvataggio versionato | Nomi dei file nel repository |

**Condizione per superarla:** **13/13 controlli** dello script.

---

## Parte C — Diagnosi e riparazione di tre stack sbagliati

**Consegna:** apri `materiali/L04_stack_sbagliato.blend` e salvalo come `consegne/L04_stack_riparato_v01.blend`. Contiene tre vaschette uguali, **Vaschetta_1**, **Vaschetta_2** e **Vaschetta_3**, ognuna con un errore diverso sui modificatori. Tutte dovrebbero misurare 80 × 50 × 20 mm con pareti da 2 mm.

**Diagnosi (prima di riparare).** Per **ciascun** oggetto scrivimi quattro punti:
1. **Difetto:** il nome (scegli tra: *ordine dei modificatori sbagliato, scala non applicata, Merge Vertices spento*, o un'altra definizione tua se pensi sia diversa);
2. **Come l'hai riconosciuto:** un numero o un'immagine (Scale in `N`, ordine nel pannello, controllo su una **copia con i modificatori applicati** come in dispensa 7.1: Non Manifold, Statistics, Merge By Distance…). Ricorda: Non Manifold sull'**originale** non è informativo;
3. **Perché succede:** **una frase causa → conseguenza** (non un elenco di etichette);
4. **Correzione:** il comando o l'impostazione che usi.

**Riparazione:** porta le tre vaschette a: stack **Mirror → Solidify**, Scale 1, mesh chiusa, un corpo, nessun vertice doppio, volume 17072 mm³. Non applicare i modificatori, non cambiare nomi né posizioni.

**Consegna:** carica `consegne/L04_stack_riparato_v01.blend` e scrivimi "consegna stack L04". Controllo con `script/verifica_L04_C.py`.

**Condizione per superarla:** 3/3 controlli dello script **e** diagnosi con **frasi causa → conseguenza**.

---

## Errori da evitare
- Lavorare sui file in `materiali/`.
- Applicare i modificatori (qui vanno lasciati attivi).
- Scordare Apply Scale prima di Solidify.
- Non attivare Even Thickness.
- Rispondere con elenchi di etichette invece che con una frase che spiega **perché**.

### Difficoltà
⭐⭐⭐⭐ (quattro stelle su cinque)
