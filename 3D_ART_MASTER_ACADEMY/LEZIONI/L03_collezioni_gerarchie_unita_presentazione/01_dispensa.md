# Lezione 3 — Collezioni, gerarchie, unità e presentazione

**Versione di riferimento:** Blender 5.0.1, interfaccia in inglese, Windows.
Scorciatoie e nomi dei menu sono stati verificati nel file ufficiale della keymap e nel codice dell'interfaccia di Blender 5.0.1. Dove una cosa è **da verificare sul tuo schermo** lo trovi scritto.

## 1. Obiettivi

Alla fine sai:
1. impostare le **unità** di una scena per lavorare in millimetri;
2. organizzare una scena con **collezioni**;
3. costruire **gerarchie** (oggetti figli di un oggetto principale);
4. dare nomi chiari e posizionare l'**origine** degli oggetti;
5. importare un'**immagine di riferimento**;
6. salvare in modo sicuro (versioni, copie di sicurezza, recupero);
7. **presentare** un oggetto con un render semplice in Eevee.

**Prerequisiti:** Lezioni 1 e 2 completate. Chiude la Fase 1.

**Perché conta per SH-Print:** un modello venduto o stampato è fatto di tante parti. Una scena disordinata, con nomi come `Cube.003` e misure in unità misteriose, fa perdere ore e produce errori di scala in stampa.

## 2. Concetti base

- **Collezione (Collection):** una "cartella" della scena. Serve a **organizzare** e a nascondere gruppi di oggetti. Non crea legami tra gli oggetti: se sposti la collezione, gli oggetti non si muovono.
- **Gerarchia (parent / figli):** un legame tra oggetti. Quando muovi, ruoti o scali il **genitore (parent)**, i **figli** lo seguono. Serve per muovere insieme le parti di un oggetto composto.
- **Empty:** oggetto "vuoto", senza geometria: un punto di riferimento. È l'ideale come genitore (*root*) di un gruppo.
- **Origine (Origin):** il punto di riferimento di un oggetto: rotazioni e scale partono da lì. Conviene metterlo dove ha senso (per esempio, a terra al centro della base).
- **Unità Blender (BU):** l'unità interna di Blender. Per default 1 BU = 1 metro.
- **Unit Scale:** il fattore che trasforma le BU in metri. Con **0.001**, 1 BU vale 1 mm: è una convenzione comune per miniature e stampa 3D, **non l'unica possibile**.
- **Immagine di riferimento:** un'immagine nello spazio 3D, usata come guida per modellare. Non fa parte del modello.

**Collezione ≠ gerarchia.** La collezione ordina; la gerarchia lega. Spesso si usano insieme.

## 3. L'Outliner

L'Outliner (in alto a destra) mostra la scena come un albero:
- **Scene Collection:** la radice. Dentro ci sono le collezioni e gli oggetti.
- Un oggetto **figlio** appare indentato sotto il suo genitore.
- Doppio clic su un nome, oppure `F2`, per rinominare.
- **Occhio:** nasconde/mostra nella viewport. **Casella accanto alla collezione:** esclude la collezione dalla scena. **Da verificare sul tuo schermo** quali colonne sono visibili (si cambiano dal menu del filtro nell'Outliner).

## 4. Collezioni

| Azione | Come |
|---|---|
| Creare una collezione | Clic destro nell'Outliner → **New Collection**; oppure seleziona oggetti, `M` → **+ New Collection** |
| Spostare oggetti in una collezione | Seleziona gli oggetti → `M` (mouse sulla viewport) → scegli la collezione |
| Collegare un oggetto a più collezioni | `Shift` + `M` |
| Rinominare | `F2` o doppio clic |
| Collezione attiva | Clic su una collezione nell'Outliner: i **nuovi oggetti** nascono lì dentro |

**Regola della lezione:** nessun oggetto deve restare fuori da una collezione, cioè direttamente sotto *Scene Collection*.

## 5. Gerarchie (parent)

### 5.1 Creare una gerarchia
1. Seleziona prima i **figli**.
2. Poi seleziona il **genitore per ultimo** (deve essere l'oggetto **attivo**, cioè con il contorno arancione chiaro). In Outliner: clic sui figli con `Ctrl` + clic, ultimo clic sul genitore.
3. Mouse sulla viewport: `Ctrl` + `P` → scegli **Object (Keep Transform)**. Se la voce ha un nome leggermente diverso, scegli quella che contiene *Keep Transform*.
4. **Verifica:** nell'Outliner i figli sono indentati sotto il genitore.

**Keep Transform** serve a non far spostare i figli al momento del collegamento. Senza, gli oggetti possono saltare in un'altra posizione.

### 5.2 Rimuovere il legame
`Alt` + `P` → **Clear and Keep Transformation**: i figli restano dove sono.

### 5.3 Provare che funziona
Seleziona il genitore, `G`, `X`, `30`, `Enter`: tutti i figli si muovono con lui. Poi `Ctrl` + `Z`.

### 5.4 Il root: un Empty
`Add → Empty → Plain Axes` crea un Empty. Si usa come genitore di tutte le parti di un oggetto. Si mette di solito **a terra, al centro della base** (così "dove l'oggetto poggia" coincide con il suo punto di riferimento).

## 6. Nomi e origine

**Nomi:** `Cube.003` non dice niente. Usa un prefisso per gruppo: `Casa_Corpo`, `Casa_Tetto`, `Albero_Tronco`. Il root si chiama `Casa_ROOT`. I nomi chiari ti fanno risparmiare tempo e permettono agli script di controllarli.

**Origine:** menu `Object → Set Origin` con queste voci (verificate in Blender 5.0.1):
- **Origin to Geometry:** l'origine va al centro della geometria;
- **Origin to 3D Cursor:** l'origine va dove si trova il 3D Cursor;
- **Geometry to Origin:** sposta la geometria attorno all'origine (non l'origine).

## 7. Unità

**Dove:** Properties editor → scheda **Scene** → pannello **Units**. Campi: **Unit System**, **Unit Scale**, **Separate Units**, **Rotation**, **Length**, **Mass**, **Time**, **Temperature**.

**Per lavorare in millimetri:**
1. Unit System: **Metric**.
2. Unit Scale: **0.001**.
3. Length: **Millimeters**.

**Effetto:** 1 BU = 1 mm. Una casa alta "60" è alta 60 mm. Nei campi con unità puoi scrivere `60` e Blender intende 60 mm.

**Fallo prima di modellare.** Cambiare le unità dopo cambia il significato dei numeri già inseriti: un oggetto largo 2 BU, prima "2 m", diventa "2 mm".

**Nota sulla stampa:** l'esportazione in STL ha le opzioni **Scale** e **Scene Unit** (verificate): ne parleremo nella Fase 6, con la tua stampante e il tuo slicer. Non ho verificato come lo slicer interpreta le unità: non dare per scontato.

## 8. Immagini di riferimento

1. Seleziona la collezione **Riferimenti** nell'Outliner (così l'immagine nasce lì).
2. Menu `Add → Image → Reference` e scegli il file.
3. Compare un piano con l'immagine nella viewport. Spostala di lato se disturba. Rinominala (es. `Rif_Casetta`).

**Perché un Empty?** L'immagine di riferimento è un Empty speciale: non è geometria del modello e **non compare nel render** (verificato su Blender 5.0.1: un render con la sola immagine davanti alla camera è completamente nero). Quindi puoi lasciarla nella scena senza rovinare la presentazione.

## 9. Salvare in sicurezza

| Azione | Comando |
|---|---|
| Salvare | `Ctrl` + `S` |
| Salvare con un nuovo nome | `Ctrl` + `Shift` + `S` (File → Save As) |
| Salvare una copia senza cambiare il file aperto | File → **Save Copy** (da verificare sul tuo schermo) |
| Recuperare dopo un crash | File → **Recover** → **Last Session** o **Auto Save** |

- **Versioni:** a ogni tappa importante salva `nome_v01`, `nome_v02`… Non sovrascrivere sempre lo stesso file.
- **`.blend1`:** Blender conserva la versione precedente (impostazione **Save Versions** = 1, verificata).
- **Auto Save:** per default ogni **2 minuti** (verificato). Non sostituisce il salvataggio manuale.
- **Cartella di backup:** una copia dei file importanti su un altro supporto (chiavetta o cloud). Un solo disco è un solo punto di guasto.

## 10. Presentare con un render semplice

### 10.1 Motore e dimensioni
- **Render Properties** (icona della fotocamera): **Render Engine → EEVEE** (nome verificato).
- **Output Properties** (icona della stampante): **Resolution X** = 1600, **Y** = 900, **%** = 100. Per default è 1920 × 1080.

### 10.2 La camera
1. Gira la vista come vuoi vedere l'oggetto.
2. Menu `View → Align View → Align Active Camera to View` (l'equivalente da tastiera è `Ctrl` + `Alt` + `Numpad 0`).
3. In alternativa: Sidebar `N` → scheda **View** → **Camera to View**: finché è attivo, muovere la vista muove la camera. **Disattivalo** quando hai finito.
4. Per guardare dalla camera: `View → Viewpoint → Camera` (`Numpad 0`).

### 10.3 Renderizzare e salvare
1. `F12`: si apre la finestra **Render Result**.
2. In quella finestra: menu `Image → Save As` (`Shift` + `Alt` + `S`).
3. Formato **PNG**, nome e cartella come richiesto.
4. Chiudi la finestra. **Salva anche il .blend**: l'immagine non è dentro il file.

### 10.4 Criteri di una buona presentazione (non solo "si vede")
- L'oggetto intero è nell'inquadratura, con un po' d'aria attorno.
- Si vedono i volumi (luce che arriva di lato, non frontale piatta).
- Non ci sono parti tagliate.
- Sfondo che non disturba.

## 11. Esempio guidato (anteprima)

Nell'esercitazione costruirai una **casetta in millimetri**, con parti in gerarchia, collezioni ordinate, un'immagine di riferimento e un render finale. Poi riordinerai da solo una scena disordinata.

## 12. Errori frequenti

| Sintomo | Causa | Soluzione |
|---|---|---|
| I figli saltano di posto quando faccio `Ctrl` + `P` | Non hai usato Keep Transform | `Ctrl` + `Z`, ripeti con **Object (Keep Transform)** |
| `Ctrl` + `P` non collega nulla | Il genitore non è l'ultimo selezionato/attivo | Deseleziona tutto, figli prima, genitore per ultimo |
| Il nuovo oggetto finisce nella collezione sbagliata | Collezione attiva diversa | Clic sulla collezione giusta prima di aggiungere, o `M` dopo |
| I numeri della scena non tornano dopo aver cambiato le unità | Hai cambiato le unità a scena già costruita | Controlla Dimensions e correggi; per il futuro imposta le unità subito |
| Il render è nero o vuoto | Camera che guarda altrove, o oggetti esclusi dalla scena | `View → Viewpoint → Camera` per controllare |
| Il render non è nella cartella | Salvato da un'altra parte | Reinvia con `Image → Save As` nella cartella giusta |
| Dopo il render il file `.blend` non contiene l'immagine | L'immagine è un file separato | Salva sempre il PNG a parte |

## 13. Checklist di verifica

- [ ] Imposto Unit System Metric, Unit Scale 0.001, Length Millimeters.
- [ ] Creo collezioni e sposto gli oggetti con `M`.
- [ ] Creo un root Empty e collego i figli con `Ctrl` + `P` (Keep Transform).
- [ ] Rinomino con prefissi chiari.
- [ ] Posiziono l'origine dove serve.
- [ ] Aggiungo un'immagine di riferimento nella collezione giusta.
- [ ] Imposto camera, Eevee e risoluzione, e salvo un PNG.
- [ ] Salvo con versioni (`_v01`, `_v02`).

## 14. Domande di ripasso

1. Che differenza c'è tra una collezione e una gerarchia?
2. Perché si usa un Empty come genitore di un gruppo di parti?
3. Cosa fa Keep Transform nel parenting?
4. Cosa significa Unit Scale 0.001? Cosa cambia se lo imposti dopo aver modellato?
5. Perché non è una buona idea lasciare oggetti chiamati `Cube.003`?
6. Il render è stato fatto, ma il file `.blend` non lo contiene: perché?
7. Quando salvi `nome_v02` invece di sovrascrivere `nome_v01`, cosa guadagni?

Le risposte sono in `03_soluzioni.md`: leggile **dopo** aver risposto.

## 15. Criteri di valutazione

Vedi `02_esercitazione.md`.
