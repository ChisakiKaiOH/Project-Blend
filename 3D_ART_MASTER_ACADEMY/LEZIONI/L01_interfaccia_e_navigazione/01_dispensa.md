# Lezione 1 — Interfaccia, navigazione e prime trasformazioni

**Versione di riferimento:** Blender 5.0.1, interfaccia in inglese, Windows.
Le scorciatoie sono state verificate nel file ufficiale della keymap di Blender 5.0.1 e i nomi dei menu nel codice dell'interfaccia. Dove una cosa è **da verificare sul tuo schermo** lo trovi scritto.

## 1. Obiettivi

Alla fine sai:
1. riconoscere le aree principali dell'interfaccia;
2. muoverti nello spazio 3D (ruotare, spostare, zoomare, cambiare vista);
3. selezionare oggetti;
4. spostare, ruotare e scalare un oggetto in modo preciso;
5. aggiungere ed eliminare oggetti;
6. salvare con nomi versionati e usare Undo.

**Prerequisiti:** Blender 5.0.1 installato e aperto. Nessuna esperienza.

## 2. Concetti base

- **Spazio 3D:** ha tre direzioni, gli assi **X** (destra/sinistra), **Y** (avanti/indietro), **Z** (su/giù). In Blender Z è l'alto. Nella viewport gli assi sono colorati: **X rosso, Y verde, Z blu**.
- **Oggetto (Object):** qualsiasi elemento della scena: forma 3D, camera, luce.
- **Viewport 3D:** la finestra centrale dove vedi e lavori sulla scena.
- **Origine:** il puntino arancione di un oggetto selezionato. È il suo "punto di riferimento": la posizione dell'oggetto è la posizione della sua origine.
- **Trasformazione:** cambiare **Location** (posizione), **Rotation** (rotazione) o **Scale** (dimensione).
- **Unità:** di default 1 unità = 1 metro (verificato: sistema Metric, scala 1.0). Il cubo iniziale è largo 2 m.
- **Object Mode:** modalità in cui lavori sugli oggetti interi. Per ora useremo solo questa.

## 3. L'interfaccia (scena iniziale)

All'avvio scegli *New → General* (o chiudi la schermata iniziale). Vedi una scena con **Camera, Cube, Light** (verificato).

| Area | Dove | A cosa serve |
|---|---|---|
| Viewport 3D | Centro | Vedere e modificare la scena |
| Outliner | Alto a destra | Elenco di tutti gli oggetti e delle collezioni |
| Properties | Basso a destra | Impostazioni dell'oggetto selezionato, materiali, render |
| Timeline | In basso | Animazione (per ora la ignoriamo) |
| Toolbar | Barra a sinistra nella viewport | Strumenti (T la mostra/nasconde) |
| Sidebar | Pannello destro della viewport | Valori numerici precisi (N la mostra/nasconde) |
| Workspace tabs | In alto | Layout, Modeling, Sculpting, UV Editing, Texture Paint, Shading, Animation, Rendering, Compositing, Geometry Nodes, Scripting |

Per ora resta sempre in **Layout**. Gli altri workspace sono configurazioni diverse delle stesse aree: li useremo nelle lezioni successive.

**Verifica:** passa il mouse su un'area e premi `N` nella viewport: compare/scompare la Sidebar. Se non succede, il mouse non era sopra la viewport (i comandi agiscono sull'area sotto il puntatore: è una regola fondamentale di Blender).

## 4. Navigare nella viewport

### 4.1 Con il mouse a tre tasti (rotellina cliccabile)

| Azione | Comando |
|---|---|
| **Orbit** (ruotare la vista) | Tieni premuto tasto centrale e muovi |
| **Pan** (spostare la vista) | `Shift` + tasto centrale e muovi |
| **Zoom** | Rotellina, oppure `Ctrl` + tasto centrale |

### 4.2 Se hai solo il touchpad del portatile (o niente tasto centrale)

Hai due soluzioni, usa **entrambe**:

**A) Navigation Gizmo** (nessuna impostazione necessaria): in alto a destra nella viewport c'è un widget con gli assi colorati.
- Trascina sugli assi: ruota la vista.
- Icona **mano**: trascinala per fare Pan.
- Icona **lente**: trascinala per fare Zoom.
- Clic su un cerchio con l'asse (X, Y, Z): vai a quella vista.

**B) Emulate 3 Button Mouse:** `Edit → Preferences → Input → Mouse → Emulate 3 Button Mouse`. Con questa opzione attiva:
- `Alt` + clic sinistro e trascina = Orbit
- `Shift` + `Alt` + clic sinistro e trascina = Pan
- `Ctrl` + `Alt` + clic sinistro e trascina = Zoom

(La combinazione dei tasti con Emulate 3 Button Mouse è quella standard di Blender: **da verificare sul tuo schermo** al primo uso.)

### 4.3 Viste standard e Numpad

Le viste frontale, laterale e dall'alto servono continuamente, perché da una sola vista non capisci le posizioni in profondità.

| Vista | Scorciatoia (tastierino) | Menu equivalente |
|---|---|---|
| Front | `Numpad 1` | `View → Viewpoint → Front` |
| Right | `Numpad 3` | `View → Viewpoint → Right` |
| Top | `Numpad 7` | `View → Viewpoint → Top` |
| Back / Left / Bottom | `Ctrl` + `Numpad 1 / 3 / 7` | `View → Viewpoint → Back / Left / Bottom` |
| Camera | `Numpad 0` | `View → Viewpoint → Camera` |
| Perspective ↔ Orthographic | `Numpad 5` | `View → Perspective/Orthographic` |
| Frame Selected (inquadra la selezione) | `Numpad .` | `View → Frame Selected` |
| Frame All (inquadra tutto) | `Home` | `View → Frame All` |

**Se non hai il tastierino numerico** (tipico dei portatili): attiva `Edit → Preferences → Input → Keyboard → Emulate Numpad`. Poi i numeri della riga in alto della tastiera si comportano come il tastierino (`1`, `3`, `7`, `0`, `5`). Il comando "Frame Selected" usa solo il punto del tastierino: dopo l'emulazione **da verificare sul tuo schermo** se `.` funziona; altrimenti usa il menu `View → Frame Selected`.

**Prospettica vs ortografica:** in prospettiva gli oggetti lontani sembrano più piccoli (come nella realtà); in ortografica no, quindi le proporzioni sono confrontabili. Per misurare e allineare si usa l'ortografica.

> Dopo aver cambiato Preferences, controlla se Blender le salva automaticamente: aprendo il menu delle Preferences, in basso a sinistra, c'è l'opzione **Auto-Save Preferences**. Se è disattivata, premi *Save Preferences* nello stesso menu.

## 5. Selezionare

| Azione | Comando |
|---|---|
| Selezionare un oggetto | Clic sinistro (diventa arancione chiaro: è quello attivo) |
| Aggiungere alla selezione | `Shift` + clic sinistro |
| Selezione a rettangolo | Con lo strumento **Select Box** (default), trascina su uno spazio vuoto |
| Selezionare tutto | `A` |
| Deselezionare tutto | `Alt` + `A` |
| Invertire la selezione | `Ctrl` + `I` |
| Selezionare dall'Outliner | Clic sul nome dell'oggetto |

**Oggetto attivo vs selezionato:** può esserci un solo oggetto *attivo* (contorno arancione chiaro, quello che mostrano le Properties); gli altri selezionati sono arancione scuro.

## 6. Trasformare (G, R, S)

Passa il mouse sulla viewport, seleziona un oggetto e usa:

| Trasformazione | Tasto | Scritta in basso |
|---|---|---|
| Move (Grab) | `G` | Translate |
| Rotate | `R` | Rotate |
| Scale | `S` | Resize |

**Procedura (esempio: spostare di 3 metri sull'asse X)**
1. Seleziona il cubo.
2. Premi `G`: il cubo segue il mouse.
3. Premi `X`: il movimento è bloccato sull'asse X (compare una linea rossa).
4. Scrivi `3` (compare in basso a sinistra).
5. Premi `Enter` per confermare.

**Annullare mentre muovi:** clic destro oppure `Esc`: l'oggetto torna dov'era.

**Valori negativi:** scrivi `-` poi il numero (`-3`).
**Numeri sulla tastiera italiana:** usa i numeri della riga in alto, il segno `-` è sul tasto accanto al punto; per i decimali Blender usa il **punto** (`0.5`), non la virgola.

**Regola:** `X`/`Y`/`Z` premuto una volta blocca *su quell'asse*; premuto due volte lavora sull'asse *locale* dell'oggetto (utile dopo averlo ruotato).

**Scrivere i valori nella Sidebar:** premi `N`, scheda **Item**, sezione **Transform**: campi **Location X/Y/Z**, **Rotation X/Y/Z** (in gradi), **Scale X/Y/Z**, **Dimensions**. Doppio clic su un campo e scrivi il valore, poi `Enter`. `Tab` passa al campo successivo.

**Attenzione alla scala:** se scali un oggetto con `S` la **Scale** diventa diversa da 1: è normale. Ricordatelo, perché in seguito (modificatori, stampa 3D) una scala diversa da 1 può dare problemi. Per questa lezione non ti serve risolverlo.

## 7. Aggiungere, eliminare, duplicare

- **Aggiungere:** `Shift` + `A` → `Mesh` → scegli (Cube, UV Sphere, Cylinder, Cone, Torus…). Compare nella posizione del **3D Cursor** (il mirino rosso e bianco, di default al centro).
  Menu equivalente: `Add → Mesh` nella barra superiore della viewport.
- **Pannello di regolazione:** subito dopo aver aggiunto un oggetto compare in basso a sinistra un pannello (es. "Add Cube"): puoi cambiare dimensione e posizione. **Sparisce appena fai altro**, quindi regolalo subito o ripeti l'operazione.
- **Eliminare:** `X` (chiede conferma) oppure `Del` (elimina subito). Menu: `Object → Delete`.
- **Rinominare:** doppio clic sul nome nell'Outliner, oppure `F2` sopra la viewport.

## 8. Salvare e annullare

- **Save:** `Ctrl` + `S`. Prima volta: scegli cartella e nome. Per le lezioni salva nella cartella `consegne/` di questa lezione (es. `consegne/L01_guidata_v01.blend`).
- **Salva con nome nuovo:** `Ctrl` + `Shift` + `S` (Save As). Ogni volta che superi una tappa importante, salva come `_v02`, `_v03`... Così se sbagli puoi tornare indietro.
- **Undo:** `Ctrl` + `Z`. **Redo:** `Ctrl` + `Shift` + `Z`. Cronologia completa: `Edit → Undo History`.
- Blender conserva di default **una copia di sicurezza** `nomefile.blend1` (opzione Save Versions = 1, verificata): se il file si rovina, rinomina il `.blend1` in `.blend`.
- Attenzione: **`Esc` o "File → New" senza salvare perdono il lavoro.** Blender avvisa, ma leggi il messaggio.

## 9. Errori frequenti

| Sintomo | Causa | Soluzione |
|---|---|---|
| Il tasto non fa nulla | Mouse sull'area sbagliata | Porta il puntatore sulla viewport |
| L'oggetto non si muove come previsto | Hai ruotato la vista e muovi "a mano" | Blocca l'asse con `X`, `Y`, `Z` o scrivi il valore |
| Hai perso la scena dalla vista | Zoom/pan troppo lontano | `Home` oppure `View → Frame All` |
| Tutto sembra distorto | Vista in prospettiva con zoom estremo | `Numpad 5` per ortografica |
| Compare un menu strano premendo `Z` | Non è un errore: è il menu di visualizzazione | `Esc` |
| L'oggetto aggiunto è lontano | Il 3D Cursor era spostato | `Shift` + `C` (riporta il cursore al centro e inquadra tutto) |

## 10. Esercizio guidato e autonomo

Vedi `02_esercitazione.md` (stessa cartella). Materiali in `materiali/`.

## 11. Checklist di verifica

- [ ] Riconosco Viewport, Outliner, Properties, Timeline, Toolbar, Sidebar.
- [ ] Ruoto, sposto e zoommo la vista senza perdermi.
- [ ] Passo da vista Front, Right, Top e Perspective alla camera.
- [ ] Seleziono uno o più oggetti e distinguo quello attivo.
- [ ] Uso G/R/S con blocco asse e valore numerico.
- [ ] Scrivo valori nella Sidebar (Item → Transform).
- [ ] Aggiungo, rinomino ed elimino un oggetto.
- [ ] Salvo con `_v01`, `_v02` e uso Undo.

## 12. Domande di ripasso

1. Qual è l'asse "alto" in Blender e di che colore è?
2. Che differenza c'è tra Object *attivo* e *selezionato*?
3. Come sposti un oggetto di esattamente 2 m su Y verso valori negativi, usando la tastiera?
4. Perché si usa la vista ortografica per allineare oggetti?
5. Cosa fai se non hai il tastierino numerico?
6. Cosa succede se premi `Esc` mentre stai muovendo un oggetto con `G`?
7. Perché conviene salvare `nome_v02.blend` e non sovrascrivere sempre lo stesso file?

Le risposte sono in `03_soluzioni.md`: leggile **dopo** aver risposto.

## 13. Criteri di valutazione della lezione

Vedi `02_esercitazione.md`. Una competenza è acquisita solo se supera la prova pratica autonoma.
