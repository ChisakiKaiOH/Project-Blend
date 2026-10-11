# Lezione 2 — Edit Mode e modellazione base

**Versione di riferimento:** Blender 5.0.1, interfaccia in inglese, Windows.
Scorciatoie e nomi dei menu sono stati verificati nel file ufficiale della keymap e nel codice dell'interfaccia di Blender 5.0.1. Dove una cosa è **da verificare sul tuo schermo** lo trovi scritto.

## 1. Obiettivi

Alla fine sai:
1. entrare e uscire dall'Edit Mode e scegliere cosa selezionare (vertici, spigoli, facce);
2. leggere i numeri di una mesh (Statistics);
3. usare Extrude, Inset, Loop Cut e Bevel con valori numerici precisi;
4. applicare la scala di un oggetto (Apply Scale);
5. riconoscere una mesh **chiusa** (manifold) e correggere i difetti più comuni;
6. costruire un oggetto con misure reali, in un solo pezzo.

**Prerequisiti:** Lezione 1 completata (navigazione, selezione, G/R/S, Sidebar).

## 2. Concetti base

- **Mesh:** la "pelle" di un oggetto 3D. È fatta di tre elementi:
  - **Vertex (vertice):** un punto;
  - **Edge (spigolo):** un segmento tra due vertici;
  - **Face (faccia):** una superficie delimitata da spigoli. Con 4 lati si chiama *quad*, con 3 *triangolo*, con più di 4 *n-gon*. Per ora usiamo i quad.
- **Object Mode / Edit Mode:** in Object Mode sposti l'oggetto intero. In **Edit Mode** modifichi la sua forma, cioè i vertici, gli spigoli e le facce.
- **Normale (normal):** la direzione "verso l'esterno" di una faccia. Il programma la usa per sapere quale lato di una faccia è fuori e quale dentro. Se è invertita, la faccia guarda all'interno.
- **Mesh chiusa (manifold):** una mesh senza buchi, in cui **ogni spigolo appartiene esattamente a due facce**. Si può "riempire d'acqua" senza perdite. È il requisito base per la stampa 3D.
- **Non-manifold:** mesh con buchi, facce interne, spigoli condivisi da 3 o più facce, o parti sospese. Può essere bellissima in render e comunque impossibile da stampare.
- **Shell (corpo):** un pezzo di mesh connesso. Un tavolo in un solo pezzo ha **1 shell**; un tavolo con le gambe "appoggiate" ma non fuse ne ha 5.
- **Estrusione (Extrude):** crea nuova geometria "tirando" una faccia, uno spigolo o un vertice. È l'operazione più usata per far crescere una forma.

## 3. Entrare nell'Edit Mode

| Azione | Comando | Menu equivalente |
|---|---|---|
| Edit Mode ↔ Object Mode | `Tab` (mouse sulla viewport, oggetto selezionato) | Menu a tendina in alto a sinistra della viewport: **Object Mode / Edit Mode** |

In Edit Mode l'oggetto cambia aspetto: compaiono vertici, spigoli e facce. Cambiano anche la barra in alto e le scorciatoie, perché ora lavori sui componenti e non sull'oggetto.

**Verifica:** premi `Tab`: gli spigoli diventano visibili e in alto a sinistra leggi *Edit Mode*. Premi di nuovo `Tab` per tornare in Object Mode.

## 4. Selezionare in Edit Mode

Il modo di selezione decide **cosa** selezioni quando fai clic.

| Modo | Pulsante (in alto, accanto al menu Mode) | Tasto | Cosa selezioni |
|---|---|---|---|
| Vertex | primo dei tre pulsanti | `1` | un punto |
| Edge | secondo | `2` | uno spigolo |
| Face | terzo | `3` | una faccia |

> **Attenzione:** se hai attivato **Emulate Numpad** (Lezione 1), i numeri della riga in alto potrebbero fare le viste e non cambiare modo di selezione. In tal caso usa **sempre i tre pulsanti** nell'intestazione. **Da verificare sul tuo schermo.**

| Azione | Comando |
|---|---|
| Selezionare | Clic sinistro |
| Aggiungere alla selezione | `Shift` + clic |
| Selezione a rettangolo | Con lo strumento **Select Box** attivo, trascina su uno spazio vuoto; oppure `B` |
| Tutto / niente / inverti | `A` / `Alt` + `A` / `Ctrl` + `I` |
| **Edge loop** (anello di spigoli) | `Alt` + clic su uno spigolo |
| Selezionare tutto ciò che è collegato | `Ctrl` + `L` (con il mouse sull'elemento) |

**Attenzione alla vista:** per default Blender seleziona solo ciò che vedi. Per vedere e selezionare anche i punti nascosti si usa **X-Ray** (`Alt` + `Z`). Non lo useremo in questa lezione: ruota la vista invece.

## 5. Leggere i numeri: Statistics

`Overlays` (menu a tendina nell'intestazione della viewport, icona con due cerchi) → spunta **Statistics**.

In basso a destra compaiono **Vertices, Edges, Faces** (e Triangles). In Edit Mode vedi anche *selezionati/totali*, es. `4/30`.

Punto di partenza: il cubo ha **8 vertici, 12 spigoli, 6 facce**. Se i numeri non coincidono con quelli attesi da questa dispensa, qualcosa non è andata come pensi: questo è il tuo strumento di controllo.

## 6. Gli strumenti di modellazione

> Prima di ogni strumento: mouse sulla viewport, Edit Mode, elemento selezionato. Dopo ogni operazione puoi **scrivere un numero** e premere `Enter`, oppure regolare i valori nel pannello **Adjust Last Operation** in basso a sinistra (si chiude quando fai un'altra cosa). Annulla sempre con `Ctrl` + `Z`.

### 6.1 Extrude (estrusione)
- **Comando:** `E`. Menu: `Mesh → Extrude`. Per le facce usa **Extrude Faces**.
- **Cosa fa:** copia le facce selezionate e le sposta lungo la loro normale, creando le pareti laterali.
- **Procedura:** seleziona una o più facce → `E` → scrivi la distanza (es. `0.42`) → `Enter`.
- **Valore positivo:** verso l'esterno. **Negativo:** verso l'interno.
- **Annullare:** se interrompi con clic destro o `Esc`, l'estrusione può restare con spessore zero (facce sovrapposte). Controlla Statistics e, se i numeri non tornano, premi `Ctrl` + `Z`. **Da verificare sul tuo schermo.**

### 6.2 Inset (rientro)
- **Comando:** `I`. Menu: `Face → Inset Faces`.
- **Cosa fa:** crea dentro la faccia selezionata una faccia più piccola, circondata da una cornice.
- **Procedura:** seleziona una faccia → `I` → scrivi lo spessore della cornice (es. `0.02`) → `Enter`. Poi puoi estrudere la faccia interna con `E`.
- **Opzioni** (pannello Adjust Last Operation): *Boundary*, *Offset Even*, *Individual* (inset separato per ogni faccia selezionata).

### 6.3 Loop Cut (taglio ad anello)
- **Comando:** `Ctrl` + `R`. Menu: strumento **Loop Cut** nella barra a sinistra.
- **Cosa fa:** aggiunge un anello di spigoli che gira attorno alla mesh, dividendo le facce.
- **Procedura:**
  1. con il mouse sulla mesh premi `Ctrl` + `R`: compare un anello **giallo** di anteprima;
  2. muovi il mouse per scegliere la direzione (l'anello cambia con lo spigolo più vicino);
  3. **ruota la rotellina** per aumentare il numero di tagli;
  4. **clic sinistro** per confermare il taglio, poi **clic destro** per lasciare i tagli equidistanti (senza scivolare);
  5. se invece muovi il mouse prima del secondo clic puoi **farli scorrere** (*slide*), poi clic per confermare.
- **Posizione precisa:** nel pannello **Adjust Last Operation** → sezione *Edge Slide* trovi il campo **Factor**, oppure seleziona l'anello con `Alt` + clic e spostalo con `G`, l'asse e un valore.
- **Perché serve:** per creare i punti dove poi faremo partire un'estrusione (gambe, bordi, incavi).

### 6.4 Bevel (smusso)
- **Comando:** `Ctrl` + `B` (spigoli). Menu: `Edge → Bevel Edges`.
- **Cosa fa:** sostituisce uno spigolo vivo con una piccola faccia smussata, che cattura la luce e fa sembrare l'oggetto più reale.
- **Procedura:** seleziona gli spigoli → `Ctrl` + `B` → muovi il mouse oppure scrivi la larghezza (es. `0.005`) → rotella per aumentare i **Segments** (più segmenti = più rotondo) → `Enter`.
- **Attenzione:** troppa larghezza vicino a spigoli ravvicinati crea geometria rovinata. Se vedi pieghe strane, riduci il valore.

### 6.5 Cancellare, unire, fondere

| Azione | Comando | Cosa succede |
|---|---|---|
| Cancellare | `X` → menu **Delete** | Vertices / Edges / Faces / Only Edges & Faces / Only Faces |
| Dissolvere | `Ctrl` + `X` | Toglie l'elemento **senza lasciare un buco** (ricuce la geometria) |
| Creare una faccia | `F` con 3 o più vertici selezionati | Riempie il buco |
| Unire vertici | `M` → **At Center / At Cursor / Collapse...** | Porta i vertici selezionati in un punto |
| Unire vertici sovrapposti | `M` → **By Distance** | Elimina i vertici doppi |

**Regola:** `X` → **Faces** lascia un buco e cancella anche gli spigoli che servivano. Per togliere una faccia senza rompere la mesh usa **Dissolve**.

## 7. Dimensioni e Apply Scale

In Lezione 1 abbiamo visto che scalare con `S` cambia il valore **Scale** dell'oggetto (non lo rimette a 1). Questo ha conseguenze in Edit Mode: alcune operazioni usano i valori **nello spazio dell'oggetto**, non in metri reali.

**Verificato su Blender 5.0.1** con un oggetto a Scale 0.15, 0.15, 0.015:
- **Extrude** di 0.1: la faccia si sposta davvero di 0.1 m (usa le misure reali);
- **Inset** di 0.1: la cornice misura solo 0.015 m (0.1 × 0.15): il valore è moltiplicato per la scala.

Quindi con Scale ≠ 1 il risultato di **Inset** non corrisponde a quello che scrivi, e con scala non uniforme (es. 0.15, 0.15, 0.015) viene anche deformato. Per **Bevel** e per i modificatori il principio è lo stesso, ma non l'ho misurato: non fidarti, applica sempre la scala. In più, per la stampa 3D le dimensioni devono essere reali e Scale deve valere 1.

**Procedura corretta:**
1. Object Mode, seleziona l'oggetto.
2. `N` → scheda **Item** → **Dimensions**: scrivi le misure reali in metri (es. 0.3, 0.3, 0.03).
3. Ora Scale è diverso da 1. Applicalo: `Ctrl` + `A` → **Scale** (menu: `Object → Apply → Scale`).
4. Controlla che **Scale = 1, 1, 1** e che Dimensions mostri le misure giuste.

Fallo **prima** di entrare in Edit Mode a modellare. Per la stampa 3D, è obbligatorio.

## 8. Normali e mesh chiusa: come controllarle

### 8.1 Controllare le normali
`Overlays` → spunta **Face Orientation**:
- **Blu** = la faccia guarda verso l'esterno (corretto);
- **Rosso** = la faccia guarda verso l'interno (da correggere).

**Correzione:** Edit Mode → `A` (seleziona tutto) → menu `Mesh → Normals → Recalculate Outside` (scorciatoia `Shift` + `N`). Per invertire solo alcune facce: `Mesh → Normals → Flip`.

Poi **disattiva** Face Orientation: serve solo per il controllo.

### 8.2 Controllare che la mesh sia chiusa
Edit Mode → modo **Vertex** o **Edge** → menu `Select → Select All by Trait → Non Manifold`. Se qualcosa si illumina, c'è un difetto. Altre voci utili in quel menu: **Loose Geometry** (vertici o spigoli sciolti), **Interior Faces** (facce dentro il solido).

**Cosa significa in pratica:**
- Se non si seleziona nulla, la mesh è chiusa.
- Se si selezionano gli spigoli intorno a un buco, manca una faccia.
- Se si selezionano più spigoli del previsto, può esserci anche un problema di **normali**.

> Questo controllo non basta da solo per dire che un modello è "pronto per la stampa": servono anche spessori, supporti e verifica nello slicer. Lo vedremo nella Fase 6.

## 9. Esempio guidato (anteprima)

Nell'esercitazione costruirai uno **sgabello** così:
1. cubo → piano sottile con Dimensions e Apply Scale;
2. Edit Mode → 2 Loop Cut per direzione sul piano;
3. Face mode → seleziona le 4 facce d'angolo in basso;
4. Extrude → 4 gambe in un solo pezzo.

Così il risultato è **un solo corpo chiuso**, adatto alla stampa, e non cinque oggetti che si toccano.

> **Errore classico:** costruire le gambe come cubi separati e metterli sotto il piano. A schermo sembra giusto, ma sono cinque corpi distinti: per stamparli dovresti poi unirli con un'operazione di fusione. Con l'estrusione il problema non nasce.

## 10. Errori frequenti

| Sintomo | Causa | Soluzione |
|---|---|---|
| I tasti `1`, `2`, `3` cambiano vista | Emulate Numpad attivo | Usa i pulsanti Vertex/Edge/Face |
| Inset o Bevel sono più piccoli o deformati rispetto al valore scritto | Scale ≠ 1 | Esci, `Ctrl` + `Z`, Apply Scale, rifai |
| Il Loop Cut non si vede | Mouse fuori dalla mesh, o Object Mode | Edit Mode, mouse sulla mesh |
| La mesh ha facce rosse in Face Orientation | Normali invertite | `Shift` + `N` in Edit Mode con tutto selezionato |
| La statistica dice più facce del previsto | Estrusione annullata a metà (spessore 0) | `Ctrl` + `Z` e rifai |
| Non riesco a selezionare una gamba | Vista da un angolo sbagliato | Usa la vista **Bottom** (`Ctrl` + `Numpad 7` o `View → Viewpoint → Bottom`) |
| Gli spigoli sembrano due ma sono uno | Vertici doppi | `M` → By Distance |

## 11. Checklist di verifica

- [ ] Entro ed esco dall'Edit Mode con `Tab`.
- [ ] Cambio modo di selezione con i pulsanti (e con i tasti, se funzionano).
- [ ] Leggo Statistics e le uso per controllare ciò che faccio.
- [ ] Uso Extrude, Inset, Loop Cut, Bevel con valori numerici.
- [ ] So applicare la scala (`Ctrl` + `A` → Scale).
- [ ] Riconosco normali invertite (rosso) e buchi (Non Manifold).
- [ ] So riparare un buco, eliminare vertici sciolti e ricalcolare le normali.

## 12. Domande di ripasso

1. Che differenza c'è tra Object Mode ed Edit Mode?
2. Cosa significa che una mesh è "manifold"? Perché serve per stampare?
3. Cosa succede se fai un Inset con Scale diverso da 1?
4. Come aggiungi esattamente due tagli equidistanti a una faccia?
5. Quale operazione scegli per togliere una faccia senza lasciare un buco: Delete o Dissolve?
6. In Face Orientation una faccia è rossa. Cosa vuol dire e come la correggi?
7. Perché non è una buona idea fare le gambe di un tavolo con cinque oggetti separati?

Le risposte sono in `03_soluzioni.md`: leggile **dopo** aver risposto.

## 13. Criteri di valutazione

Vedi `02_esercitazione.md`. Una competenza è acquisita solo se supera la prova pratica autonoma e la riparazione.
