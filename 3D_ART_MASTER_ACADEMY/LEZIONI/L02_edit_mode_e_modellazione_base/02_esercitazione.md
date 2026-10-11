# Esercitazione L02 — Sgabello, tavolino e riparazione

**Livello:** 2 (principiante) · **Tempo indicativo:** guidata 60–75 min, autonoma 30–45 min, riparazione 20 min
**Strumenti:** Blender 5.0.1, `materiali/L02_start.blend`, `materiali/L02_mesh_difettosa.blend`
**Dispensa:** `01_dispensa.md`

Il lavoro si divide in tre parti. Salva sempre con nomi versionati (`_v01`, `_v02`, …) nella cartella `consegne/` di questa lezione. **Non modificare i file in `materiali/`.**

Scena di partenza (`L02_start.blend`): un cubo arancione di 2 m chiamato **Sgabello** (a sinistra), un cubo azzurro di 2 m chiamato **Tavolino** (a destra) e il Pavimento. Nella Parte A lavori solo sullo Sgabello, nella Parte B solo sul Tavolino. **Non rinominare gli oggetti.**

---

## Parte A — Modalità guidata: lo Sgabello

**Obiettivo:** costruire uno sgabello 0,30 × 0,30 × 0,45 m in **un solo pezzo chiuso**. Riferimento visivo: `materiali/L02_riferimento_A.png`.

### A0. Preparazione
1. Apri `materiali/L02_start.blend` e salvalo subito come `consegne/L02_guidata_v01.blend` (File → Save As).
2. Verifica che nel Outliner ci siano **Sgabello** e **Tavolino**.

### A1. Il piano: Dimensions e Apply Scale (Object Mode)
1. Clicca lo **Sgabello**. Mouse sulla viewport, premi `N` → scheda **Item**.
2. In **Dimensions** scrivi: X `0.3`, Y `0.3`, Z `0.03`.
3. Ora **Scale** vale 0.15, 0.15, 0.015. Applicalo: `Ctrl` + `A` → **Scale** (o menu `Object → Apply → Scale`).
4. **Risultato atteso:** Scale = 1, 1, 1 e Dimensions = 0.3, 0.3, 0.03. Usa `View → Frame Selected` per inquadrarlo.

### A2. Entra in Edit Mode e accendi Statistics
1. `Tab` (o menu Mode → Edit Mode).
2. `Overlays` → spunta **Statistics**.
3. **Risultato atteso:** 8 vertici, 12 spigoli, 6 facce.

### A3. Due Loop Cut per direzione
1. Mouse sulla mesh, `Ctrl` + `R`. Muovi il mouse finché l'anello giallo divide il piano in strisce lungo una direzione.
2. Ruota la rotellina fino a **2** tagli, **clic sinistro**, poi **clic destro** (tagli equidistanti).
3. Ripeti nella direzione perpendicolare (anello giallo che divide nell'altra direzione).
4. **Risultato atteso:** **32 vertici, 60 spigoli, 30 facce**. Il piano appare diviso in una griglia 3 × 3 sopra e sotto.
5. Se i numeri non coincidono: `Ctrl` + `Z` e riprova. Non andare avanti.

### A4. Seleziona le facce d'angolo in basso
1. Passa al modo **Face** con il terzo pulsante nell'intestazione (usa il pulsante: i tasti numerici possono fare le viste).
2. Vista dal basso: `View → Viewpoint → Bottom` (`Ctrl` + `Numpad 7`).
3. Clic su una faccia d'angolo, poi `Shift` + clic sulle altre tre.
4. **Risultato atteso:** Statistics mostra **Faces 4/30**.

### A5. Estrudi le gambe
1. `E`, scrivi `0.42`, `Enter`.
2. **Risultato atteso:** **48 vertici, 92 spigoli, 46 facce**. Se vedi un numero diverso, `Ctrl` + `Z` e rifai.
3. Ruota la vista: devi vedere quattro gambe quadrate.

### A6. Appoggia lo sgabello al pavimento
1. `Tab` per tornare in Object Mode.
2. In `N` → Item → **Location Z**, scrivi `0.435`.
3. **Perché 0.435?** L'origine è al centro del piano. Il piano è spesso 0,03 m (mezzo spessore = 0,015) e le gambe scendono di altri 0,42: in totale 0,015 + 0,42 = 0,435 m sotto l'origine. Quindi l'origine va a 0,435 m da terra.
4. **Risultato atteso:** Dimensions = 0.3 × 0.3 × 0.45.

### A7. Inset e incavo sul piano
1. Edit Mode, modo Face, vista dall'alto (`View → Viewpoint → Top`).
2. Seleziona **solo la faccia centrale** del piano (quella al centro della griglia 3 × 3).
3. `I`, scrivi `0.02`, `Enter` (cornice di 2 cm).
4. `E`, scrivi `-0.005`, `Enter` (incavo di 5 mm verso l'interno).
5. **Risultato atteso:** **56 vertici, 108 spigoli, 54 facce**.

### A8. Bevel di prova (fuori dallo sgabello)
Per non rovinare lo sgabello, prova il bevel su un cubo separato.
1. **Object Mode** → `Shift` + `A` → `Mesh` → `Cube` (il cubo di 2 m va benissimo).
2. `Tab`, `A` (tutto selezionato), `Ctrl` + `B`, scrivi `0.1`, ruota la rotellina fino a **3 segmenti**, `Enter`.
3. **Risultato atteso:** **96 vertici, 192 spigoli, 98 facce**. Gli spigoli ora sono arrotondati.
4. Cancella il cubo di prova: Object Mode, selezionalo, `X` → Delete.

### A9. Controllo e salvataggio
1. Face Orientation: `Overlays` → **Face Orientation**. Tutto deve essere **blu**. Poi disattivala.
2. Salva come `consegne/L02_guidata_v02.blend`.
3. Carica il file e scrivimi "consegna guidata L02" per il controllo con lo script (`script/verifica_L02.py -- A`).

---

## Parte B — Modalità autonoma: il Tavolino (prova di superamento)

**Consegna:** apri di nuovo `materiali/L02_start.blend`, salvalo come `consegne/L02_autonoma_v01.blend` e trasforma il **Tavolino** in un tavolino 0,60 × 0,40 × 0,45 m. Riferimento visivo: `materiali/L02_riferimento_B.png`.

**Requisiti (tutti misurati dallo script):**

| # | Requisito |
|---|---|
| 1 | Oggetto chiamato **Tavolino**, senza modificatori |
| 2 | **Scale = 1** e rotazione 0 (Apply fatto) |
| 3 | Dimensioni **0,60 × 0,40 × 0,45 m** (tolleranza 1 cm) |
| 4 | Base appoggiata al pavimento (Z minima = 0, tolleranza 1 cm) |
| 5 | Mesh **chiusa**: nessuno spigolo non-manifold, nessun vertice sciolto |
| 6 | **Un solo corpo**: le gambe sono parte della stessa mesh del piano |
| 7 | **Normali verso l'esterno** |
| 8 | Nessun vertice doppio |
| 9 | **4 gambe**, una per angolo, a filo con gli angoli del piano, sezione **4 × 4 cm** (tolleranza 1,5 cm) |
| 10 | Spessore del piano **3 cm** (tolleranza 1 cm) |

**Non ti do i passaggi.** Hai a disposizione la dispensa e l'esperienza della Parte A. L'unica difficoltà nuova: le gambe sono sottili (4 cm), quindi i tagli **non possono essere equidistanti**. Come posizioni un Loop Cut a una distanza esatta dal bordo?

**Aiuti (leggili solo se ti blocchi):**

- Il pannello **Adjust Last Operation** dopo un Loop Cut contiene un campo per spostare il taglio.
- In alternativa: seleziona l'anello di spigoli con `Alt` + clic e spostalo con `G`, l'asse e un valore.
- Controlla sempre Statistics: dopo i tagli e le estrusioni i numeri devono corrispondere a quelli della Parte A (32/60/30 e poi 48/92/46), perché la topologia è la stessa.

**Consegna:** carica `consegne/L02_autonoma_v01.blend` (e le versioni successive) e scrivimi "consegna L02".

### Criteri di superamento

| Criterio | Come lo verifico |
|---|---|
| Requisiti 1–10 | `script/verifica_L02.py -- B` |
| Scena ordinata (nessun oggetto di troppo, nomi originali) | Outliner |
| Salvataggio versionato | Nomi dei file nel repository |

**Condizione per superarla:** 10/10 controlli dello script. Un singolo controllo fallito non supera la prova: ti dico quale e come correggerlo, e ripeti.

---

## Parte C — Diagnosi e riparazione

**Consegna:** apri `materiali/L02_mesh_difettosa.blend` e salvalo come `consegne/L02_riparata_v01.blend`. Contiene un cubo chiamato **Difettoso** con alcuni problemi.

**Diagnosi** (scrivimi le risposte, prima di riparare):
1. Edit Mode, Statistics acceso, niente selezionato: quanti vertici, spigoli e facce vedi?
2. Quante facce ha un cubo chiuso? Quale faccia manca?
3. `Select → Select All by Trait → Loose Geometry`: quanti vertici vengono selezionati?
4. `Overlays → Face Orientation`: quale faccia è rossa? (Guarda in vista Front.)
5. `Select → Select All by Trait → Non Manifold` (in modo Edge): perché si illuminano più spigoli di quelli del buco?
6. In una frase: perché questo modello non si può stampare?

**Riparazione:** porta il cubo a 8 vertici, 12 spigoli e 6 facce, chiuso, con normali verso l'esterno, senza modificatori. Il cubo non deve cambiare nome o dimensione.

**Consegna:** carica `consegne/L02_riparata_v01.blend` e scrivimi "consegna riparazione L02". Lo controllo con `script/verifica_L02_C.py`.

**Condizione per superarla:** 6/6 controlli dello script.

---

## Errori da evitare
- Lavorare sui file in `materiali/` (salva sempre una copia).
- Modellare con Scale ≠ 1.
- Fare le gambe come cubi separati, anche se "sembra" giusto.
- Andare avanti quando i numeri di Statistics non coincidono con quelli attesi.

### Difficoltà
⭐⭐⭐ (tre stelle su cinque)
