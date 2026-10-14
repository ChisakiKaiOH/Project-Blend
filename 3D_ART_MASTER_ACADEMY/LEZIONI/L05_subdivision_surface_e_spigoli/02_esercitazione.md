# Esercitazione L05 — Blocco, sapone e tre blocchi sbagliati

**Livello:** 3 · **Tempo indicativo:** guidata 45–60 min, autonoma 45–60 min, riparazione 30 min
**Strumenti:** Blender 5.0.1, file in `materiali/`
**Dispensa:** `01_dispensa.md`

Salva sempre con nomi versionati (`_v01`, `_v02`, …) in `consegne/`. **Non modificare i file in `materiali/`.** Unità: **1 unità Blender = 1 mm**. In questa lezione **non applichi** Subdivision Surface: lo lasci attivo.

> **Regola della lezione.** Prima di caricare un file, leggi la **tabella dei requisiti** della parte e spunta riga per riga. I **nomi degli oggetti** sono la prima riga: sono la causa di quasi tutti i punti persi nelle lezioni precedenti.

---

## Parte A — Modalità guidata: il blocco e il blocco con Crease

**Obiettivo:** due cubi da 40 mm con spigoli arrotondati, uno costruito con i **supporti** e uno con il **Crease**. Riferimento: `materiali/L05_riferimento_A.png` (il blocco con i supporti).

### A0. Preparazione
1. Apri `materiali/L05_start.blend` e salvalo come `consegne/L05_guidata_v01.blend`.
2. La scena ha unità in mm e due collezioni: **Scena** (Camera, Sole, Pavimento) e **Modello** (vuota).

### A1. Il cubo
1. Clic sulla collezione **Modello**. `Shift` + `C`. `Add → Mesh → Cube`.
2. In `N` → Item: **Dimensions** `40`, `40`, `40`. `Ctrl` + `A` → **Scale**.
3. **Location** `0`, `0`, `20`. Rinomina **Blocco** (`F2`).
4. **Verifica:** Scale 1, il cubo poggia sul pavimento.

### A2. Subdivision senza supporti
1. Con **Blocco** selezionato: Properties → scheda **Modifiers** → `Add Modifier → Generate → Subdivision Surface`. Imposta **Levels Viewport** a `2` e **Render** a `3`. (Scorciatoia `Ctrl` + `2` con il mouse sulla viewport: sul tuo PC non ha funzionato, quindi usa il metodo manuale.)
2. Il cubo è diventato una forma simile a una sfera. È normale: dispensa 2.2.
3. Controlla che **Render** sia `3` (il valore predefinito è 2).

### A3. Misura sulla copia (prima del rimedio)
1. `Shift` + `D`, clic destro. Sulla copia: menu del modificatore → **Apply**.
2. Overlays → Statistics e `N` → Dimensions.
3. **Risultato atteso:** **98 vertici, 96 facce**, dimensioni circa **33,58 mm** su ogni asse.
4. **Annota** le dimensioni e i conteggi (servono alla frase finale). Poi elimina la copia (`X`).

### A4. Supporti con Inset individuale
1. `Tab`, modo **Face**, `A`. `I`, `4`, `Enter`.
2. Pannello in basso a sinistra (**Inset Faces**): attiva **Individual**.
3. **Risultato atteso** (Statistics in Edit Mode): **32 vertici, 60 spigoli, 30 facce**.
4. `Tab` per tornare in Object Mode.

### A5. Misura sulla copia (dopo il rimedio)
1. Come A3: copia → **Apply** sul duplicato → Dimensions.
2. **Risultato atteso:** **40 × 40 × 40 mm**. La forma ha spigoli smussati ma le facce sono piatte e intere.
3. Elimina la copia.

### A6. Prova (facoltativa)
Con `Tab` e un nuovo Inset (cambia il valore: `2`, poi `6`) guarda cosa fa al raccordo. Poi riporta a `4` (`Ctrl` + `Z` o reimposta).

### A7. Shade Smooth
Object Mode, **Blocco** selezionato: menu **Object → Shade Smooth**.

### A8. Il secondo blocco, con il Crease
1. Collezione **Modello** attiva, `Shift` + `C`, `Add → Mesh → Cube`. Dimensions `40, 40, 40`, `Ctrl` + `A` → **Scale**. Location `70`, `0`, `20`. Rinomina **Blocco_crease**.
2. Aggiungi il modificatore come in A2: **Levels Viewport** `2`, **Render** `3`.
3. `Tab`, modo **Edge**, `A`. `Shift` + `E`, scrivi `0.5`, `Enter`.
4. Per vedere i crease: Overlays (in Edit Mode) → **Crease**.
5. `Tab`. Menu **Object → Shade Smooth**.
6. **Risultato atteso:** simile al primo blocco, con una mesh di base di soli 8 vertici.

### A9. Requisiti da spuntare prima di caricare

| # | Requisito | ✓ |
|---|---|---|
| 1 | Oggetti chiamati esattamente **Blocco** e **Blocco_crease** | ☐ |
| 2 | Entrambi nella collezione **Modello**, nessun oggetto nella radice della scena | ☐ |
| 3 | **Scale 1**, rotazione 0 | ☐ |
| 4 | Un solo modificatore **Subdivision**, **Viewport 2**, **Render 3**, non applicato | ☐ |
| 5 | **Blocco**: mesh di base solo quad, Individual attivo, 32 vertici | ☐ |
| 6 | **Blocco_crease**: base di 8 vertici, **Crease 0,5** sui 12 spigoli | ☐ |
| 7 | Shade Smooth su entrambi | ☐ |
| 8 | Dimensioni finali 40 × 40 × 40 e Z minima 0 | ☐ |
| 9 | Unità in mm | ☐ |

Salva come `consegne/L05_guidata_v02.blend` e scrivimi "consegna guidata L05". La controllo con `script/verifica_L05.py -- A`.

---

## Parte B — Modalità autonoma: il sapone (prova di superamento)

**Consegna:** apri di nuovo `materiali/L05_start.blend`, salvalo come `consegne/L05_autonoma_v01.blend` e costruisci un **sapone** 80 × 50 × 20 mm, con gli spigoli arrotondati e un **incavo** per l'etichetta sulla faccia superiore. Riferimento: `materiali/L05_riferimento_B.png`.

**Requisiti (misurati dallo script sulla mesh dopo il modificatore). Spunta riga per riga prima di caricare:**

| # | Requisito | ✓ |
|---|---|---|
| 1 | Oggetto chiamato esattamente **Sapone**, nella collezione **Modello**, nulla fuori dalle collezioni | ☐ |
| 2 | **Scale 1**, rotazione 0 | ☐ |
| 3 | Un solo modificatore **Subdivision**, **Viewport 2**, **Render 3**, **non applicato** | ☐ |
| 4 | Mesh di base: **solo quad** | ☐ |
| 5 | Mesh di base: **80 × 50 × 20 mm**, centrata su X e Y (origine nel centro), **Z da 0 a 20** | ☐ |
| 6 | Incavo sulla faccia superiore: nella **base** le pareti sono a **X ±25** e **Y ±10** (50 × 20 mm), **profondità 1,5 mm** (fondo a Z = 18,5) | ☐ |
| 7 | Dimensioni **finali** 80 × 50 × 20 mm (gli spigoli esterni hanno supporti) | ☐ |
| 8 | Spigoli arrotondati: **volume** tra **68 500 e 75 500 mm³** | ☐ |
| 9 | Il fondo dell'incavo resta a Z = 18,5 (±0,4) | ☐ |
| 10 | Il bordo dell'incavo è **netto**: a 3 mm dentro il bordo la superficie è ≤ 18,8 mm, a 1–3 mm fuori è piatta (≥ 19,93 mm) | ☐ |
| 11 | **Shade Smooth** su tutte le facce | ☐ |
| 12 | Mesh finale **chiusa**, **1 corpo**, nessun vertice doppio | ☐ |
| 13 | Unità in mm | ☐ |

**Non ti do i passaggi.** Pensa a dove servono gli anelli di supporto: lungo gli spigoli esterni e intorno all'incavo, **sia sul bordo sia sul fondo**.

**Aiuti (leggili solo se ti blocchi):**
- Per i bordi esterni vale la tecnica di A4. Quanto distano i supporti dallo spigolo? Guarda la tabella 4.2 della dispensa: per avere il volume nella finestra del requisito 8 funzionano distanze tra 2 e 6 mm.
- Per l'incavo ti servono: una **faccia** sulla parte superiore (quella interna, dopo il primo Inset), un contorno che arrivi a **X ±25, Y ±10**, un **Extrude** verso il basso di 1,5 mm e un anello di supporto anche sul fondo.
- Il bordo dell'incavo è netto solo se c'è un anello **vicino al bordo** (a circa 1,5 mm) fuori dall'incavo e uno sul fondo.
- Il volume del requisito 8 non lo vedi in Blender: controlla invece le dimensioni finali sulla copia (requisito 7) e la forma a occhio.

**Consegna:** carica `consegne/L05_autonoma_v01.blend` (e le successive) e scrivimi "consegna L05".

### Criteri di superamento

| Criterio | Come lo verifico |
|---|---|
| Requisiti 1–13 | `script/verifica_L05.py -- B` (16 controlli) |
| Salvataggio versionato | Nomi dei file nel repository |

**Condizione per superarla:** **16/16 controlli** dello script.

---

## Parte C — Diagnosi e riparazione di tre blocchi sbagliati

**Consegna:** apri `materiali/L05_blocchi_sbagliati.blend` e salvalo come `consegne/L05_blocchi_riparati_v01.blend`. Contiene tre cubi da 40 mm, **Blocco_1**, **Blocco_2** e **Blocco_3**, con un errore diverso ciascuno. Tutti dovrebbero avere il **volume** nella finestra 55 000–60 200 mm³ (come il blocco della Parte A), dimensioni 40 × 40 × 40 e ombreggiatura Smooth.

**Diagnosi (prima di riparare).** Per **ciascun** oggetto scrivimi quattro punti:
1. **Difetto:** il nome (scegli tra: *nessun supporto, Crease troppo forte, ombreggiatura Flat, livelli sbagliati*, o una definizione tua);
2. **Come l'hai riconosciuto:** un numero o un'immagine (Dimensions sulla copia con Apply, Statistics, overlay Crease, aspetto della superficie);
3. **Perché succede:** **una frase** nel formato **"Poiché [cosa succede nel programma], [effetto], quindi [conseguenza misurabile]"**;
4. **Correzione:** il comando o l'impostazione che usi.

**Riparazione:** porta i tre blocchi a: **Subdivision livello 2 non applicato**, **Smooth**, base solo quad, **40 × 40 × 40 mm** finali, spigoli arrotondati (volume nella finestra), mesh chiusa. Scale 1. **Non cambiare nomi né posizioni.**

### Requisiti da spuntare prima di caricare

| # | Requisito | ✓ |
|---|---|---|
| 1 | Oggetti chiamati **Blocco_1**, **Blocco_2**, **Blocco_3** (non rinominati) | ☐ |
| 2 | Posizioni invariate (X −70 / 0 / +70, Z 20) | ☐ |
| 3 | Scale 1 | ☐ |
| 4 | Un solo modificatore **Subdivision**, **Viewport 2**, non applicato | ☐ |
| 5 | Shade Smooth su tutti e tre | ☐ |
| 6 | Dimensioni finali 40 × 40 × 40 (controllate su una copia con Apply) | ☐ |

**Consegna:** carica `consegne/L05_blocchi_riparati_v01.blend` e scrivimi "consegna blocchi L05". Controllo con `script/verifica_L05_C.py`.

**Condizione per superarla:** 3/3 controlli dello script **e** diagnosi con **frasi causa → conseguenza**.

---

## Errori da evitare
- Rinominare male gli oggetti (rileggi la tabella).
- Applicare il modificatore (qui resta attivo).
- Dimenticare Shade Smooth.
- Scrivere elenchi di etichette invece di frasi che spiegano **perché**.
- Correggere la forma scalando l'oggetto: va corretta la geometria (supporti), non la scala.

### Difficoltà
⭐⭐⭐⭐ (quattro stelle su cinque)
