# Lezione 4 — Modificatori: Mirror, Solidify, Array

**Versione di riferimento:** Blender 5.0.1, interfaccia in inglese, Windows. Unità: 1 unità Blender = 1 mm.
Comportamenti e valori di questa lezione sono stati **misurati** su Blender 5.0.1; i nomi dei menu e le scorciatoie sono stati verificati nel codice e nella keymap della 5.0.1. Dove una cosa è **da verificare sul tuo schermo** lo trovi scritto.

## 1. Obiettivi

Alla fine sai:
1. aggiungere, configurare e riordinare un **modificatore**;
2. usare **Mirror** per modellare solo metà di un oggetto simmetrico;
3. usare **Solidify** per dare spessore a una superficie, con spessore reale in millimetri;
4. usare **Array** per ripetere un oggetto (per esempio più copie sul piatto di stampa);
5. spiegare **perché l'ordine dei modificatori conta**;
6. riconoscere e correggere tre errori tipici (ordine, scala, Merge).

**Prerequisiti:** Lezioni 1–3 completate (Edit Mode, Apply Scale, mesh chiusa, unità in mm, collezioni).

**Perché conta per SH-Print:** con i modificatori modelli la metà e ottieni l'intero; imposti lo spessore delle pareti una volta sola e puoi cambiarlo dopo; ripeti una forma per riempire il piatto di stampa. Ma un ordine sbagliato o una scala non applicata producono pareti sottili o mesh non chiuse **senza che tu te ne accorga a occhio**.

## 2. Concetti base

- **Modificatore (modifier):** un'operazione applicata a una mesh **senza cambiare i suoi vertici originali**. Si vede il risultato, ma la mesh di partenza resta intatta. È *non distruttivo*: puoi cambiare i parametri o rimuovere il modificatore quando vuoi.
- **Stack dei modificatori:** l'elenco dei modificatori di un oggetto. Si calcolano **dall'alto verso il basso**: il risultato di uno è l'input del successivo. **L'ordine conta.**
- **Applicare un modificatore (Apply):** trasforma il risultato in vera geometria e lo toglie dallo stack. È **irreversibile** (a parte `Ctrl` + `Z`). In questa lezione **non applichiamo** nulla: lo vedremo nella Lezione 8.
- **Mesh di partenza vs mesh finale:** la mesh che vedi in Edit Mode è quella di partenza; quella che si stampa è il **risultato dei modificatori**. Per questo i controlli di questa lezione guardano la mesh *dopo* i modificatori.

## 3. Dove trovare i modificatori

Properties editor → scheda **Modifiers** (icona della chiave inglese). Pulsante **Add Modifier** → categoria **Generate** → scegli:
- **Mirror**
- **Solidify**
- **Array** (nella 5.0.1 la voce **Array** è un asset basato su Geometry Nodes; accanto c'è **Array (Legacy)**, il modificatore classico. Le due versioni hanno parametri diversi: sotto trovi entrambe.)

Ogni modificatore ha un pannello con il nome, i pulsanti di visibilità (monitor = viewport, fotocamera = render), un menu a discesa e i parametri.

| Azione | Come |
|---|---|
| Cambiare l'ordine | Trascina il pannello dalla maniglia a destra; oppure menu a discesa del modificatore → **Move to First** / **Move to Last** (da verificare sul tuo schermo i nomi esatti delle voci) |
| Applicare | Menu a discesa → **Apply**, oppure `Ctrl` + `A` con il mouse sul pannello (non lo faremo) |
| Rimuovere | Pulsante `X` sul pannello, o menu a discesa → **Delete** |
| Nascondere nella viewport | Pulsante a forma di monitor |

## 4. Mirror: modellare la metà

**Cosa fa:** riflette la mesh rispetto a un piano passante per l'**origine dell'oggetto**, con l'asse scelto.

**Parametri (nomi verificati):**
- **Mirror Axis:** X, Y, Z. Di default è attivo **X**.
- **Merge Vertices** (default **attivo**) e **Merge Distance** (0.001): fonde i vertici sul piano di specchio.
- **Clip:** impedisce ai vertici di attraversare il piano mentre li sposti.

**Regole fondamentali:**
1. **L'origine dell'oggetto deve stare sul piano di specchio.** Per questo si usa `Object → Set Origin → Origin to 3D Cursor` con il 3D Cursor al centro (`Shift` + `C`).
2. **Elimina la faccia che giace sul piano di specchio**, altrimenti resta un muro interno al centro. Si cancella con `X` → **Faces** (vedi 4.1).
3. Tieni **Merge Vertices** attivo: serve a unire le due metà in un solo corpo chiuso.

### 4.1 Delete → Faces o Only Faces?
Nella Lezione 2 hai visto il menu Delete (`X`). Qui la differenza si vede: se cancelli due facce adiacenti con **Only Faces**, lo spigolo che le univa **resta come spigolo sciolto** (senza facce). Misurato nell'esempio della lezione: **2 spigoli non-manifold** nella mesh finale. Con **Faces** lo spigolo sparisce. Per cancellare facce usa **Faces**.

## 5. Solidify: dare spessore

**Cosa fa:** trasforma una superficie (senza spessore) in un solido, spostando una copia lungo le **normali**.

**Parametri (nomi verificati):**
- **Thickness:** spessore. **È in unità dell'oggetto**: con Scale 1 e 1 BU = 1 mm, `2` significa 2 mm.
- **Offset:** dove cresce lo spessore. **-1** (default): verso l'interno, rispetto alle normali; **+1**: verso l'esterno; **0**: a cavallo della superficie.
- **Even Thickness:** mantiene lo spessore costante negli angoli. **Va attivato** (di default è spento).
- **Fill Rim** (default attivo): chiude il bordo della superficie.

**Misure sull'esempio della lezione** (vaschetta 80 × 50 × 20 mm, pareti da 2 mm, Offset -1):

| Impostazione | Volume del solido |
|---|---|
| **Even Thickness attivo** | **17072 mm³** (corretto) |
| Even Thickness spento | 11876 mm³ (circa **30% in meno**: pareti più sottili negli angoli) |

Il volume corretto si ricava a mano: 80 × 50 × 20 − 76 × 46 × 18 = 17072 mm³ (esterno meno cavità).

**Offset e normali:** con Offset -1 la vaschetta mantiene le dimensioni esterne di 80 × 50 × 20 mm perché lo spessore cresce verso l'interno. Per una lastra piana con le normali verso l'alto, serve invece **Offset +1** se vuoi che lo spessore cresca verso l'alto (da Z = 0 a Z = spessore).

**Scala dell'oggetto:** Thickness segue la scala dell'oggetto. Misurato: con Scale 0.5 e Thickness 2, le pareti diventano di **1 mm** (volume 8864 mm³ invece di 17072). Applica sempre la scala (`Ctrl` + `A` → Scale) **prima** di usare Solidify.

## 6. Array: ripetere

**Cosa fa:** crea copie della mesh a distanza regolare.

### 6.1 Array (nuovo, asset Geometry Nodes) — la voce "Array" del menu
Parametri principali (valori predefiniti verificati):
- **Shape:** **Line** (default). Ci sono anche opzioni per disporre le copie in cerchio o lungo una curva: non le usiamo.
- **Count Method / Count:** Count, con **Count = 3**.
- **Offset Method:** **Relative** (default).
- **Offset:** (1, 0, 0). **È relativo alla dimensione dell'oggetto in input**, non in millimetri: `1` = una copia attaccata a quella precedente; `1.2` = una distanza pari al 20% della larghezza.
- **Realize Instances:** attivo (serve perché il risultato sia una vera mesh).
- **Merge:** spento. Le copie restano **corpi separati**.

**Formula per lasciare un vuoto di G mm tra copie larghe L mm:**

> Offset X = (L + G) / L

Esempio verificato: vaschetta larga 80 mm, vuoto 10 mm → Offset X = 90 / 80 = **1.125** → le tre copie hanno un passo di 90 mm e il gruppo misura 80 + 90 + 90 = **260 mm**.

### 6.2 Array (Legacy) — alternativa classica
Parametri (nomi verificati): **Fit Type** = Fixed Count, **Count** (default 2), **Relative Offset** (acceso di default, X = 1), **Constant Offset** (spento di default) con **Constant Offset Displacement**, **Merge Vertices** (spento).
Per ottenere lo stesso risultato: Count **3**, **Relative Offset spento**, **Constant Offset acceso** con X = **90** (mm).

### 6.3 Copie separate: va bene per il piatto di stampa
Con **Merge spento** ogni copia è un corpo chiuso a sé. Per stampare più copie dello stesso pezzo nello stesso lavoro va benissimo, purché restino **separate** da un vuoto sufficiente. Se invece le copie dovessero toccarsi per formare **un solo pezzo**, servirebbe un'unione: lo vedremo più avanti, in Fase 6.

## 7. L'ordine dei modificatori

**Ordine corretto per un oggetto simmetrico con spessore ripetuto:** **Mirror → Solidify → Array.**

- **Mirror prima di Solidify:** prima ricostruisci l'intera forma, poi le dai spessore. Se Solidify viene **prima**, dà spessore alla metà e chiude anche il bordo sul piano di specchio: dopo il Mirror la mesh **non risulta più chiusa** (misurato: 8 spigoli non-manifold nella vaschetta singola).
- **Array per ultimo:** ripete il risultato finale.

**Misure nell'esempio della lezione:**

| Configurazione | Risultato misurato |
|---|---|
| Mirror → Solidify (corretto) | mesh chiusa, 1 corpo, volume 17072 mm³ |
| Solidify → Mirror | **8 spigoli non-manifold** nella vaschetta singola (24 con le tre copie): mesh non chiusa |
| Mirror con **Merge Vertices spento** | **2 corpi** separati e **8 vertici doppi** sul piano di specchio |
| Mirror → Solidify → Array, 3 copie | **3 corpi** chiusi, volume totale 51216 mm³, 72 vertici, 132 spigoli, 66 facce |

### 7.1 Come controllare la mesh finale (su una copia)
`Select → Select All by Trait → Non Manifold` lavora sulla **mesh di partenza**, non sul risultato dei modificatori. Misurato su tre vaschette sbagliate: sull'oggetto originale seleziona **sempre 6 spigoli** (i bordi aperti della metà) e quindi **non dice nulla** sulla mesh che stamperai.

Per controllare il risultato:
1. Seleziona l'oggetto, `Shift` + `D` e poi clic destro (duplica senza spostare). Il duplicato ha una mesh propria.
2. Sul **duplicato** applica i modificatori **dall'alto verso il basso**: per ciascuno menu a discesa → **Apply**.
3. `Tab` (Edit Mode), modo **Edge**: `Select → Select All by Trait → Non Manifold` e leggi Statistics.
4. `A` poi `M` → **By Distance**: in basso compare un messaggio con il numero di vertici rimossi.
5. Esci con `Tab` e **elimina il duplicato** (`X`).

**Numeri di riferimento sulla vaschetta singola (Mirror → Solidify):** una copia corretta ha **24 vertici, 44 spigoli, 22 facce**, nessuno spigolo non-manifold e **0 vertici rimossi** da Merge By Distance. Con l'ordine sbagliato (Solidify → Mirror) la copia ha 46 spigoli e 25 facce, con **8 spigoli non-manifold**. Con Merge spento ha **32 vertici** e Merge By Distance ne rimuove **8**.

**Attenzione:** una scala non applicata (Scale ≠ 1) **non lascia tracce nei conteggi**: la copia ha i numeri giusti (24/44/22) ma le pareti sono più sottili. Si riconosce guardando **Scale** in `N`.

## 8. Procedura tipica (anteprima dell'esercitazione)

1. Modella **solo metà** dell'oggetto, con l'origine sul piano di specchio.
2. Elimina la faccia sul piano di specchio con `X` → **Faces**.
3. Applica la scala; Mirror; Solidify (con Even Thickness); Array.
4. Controlla le **dimensioni finali** e il **volume**, non solo l'aspetto.

## 9. Errori frequenti

| Sintomo | Causa | Soluzione |
|---|---|---|
| Mesh non chiusa dopo i modificatori (spigoli non-manifold) | Solidify prima di Mirror, oppure faccia sul piano di specchio non eliminata | Metti Mirror prima di Solidify; elimina la faccia con `X` → Faces |
| Le due metà non si uniscono (due corpi) | Merge Vertices spento, o origine fuori dal piano di specchio | Attiva Merge Vertices; Origin to 3D Cursor |
| Pareti più sottili del previsto | Scale ≠ 1, oppure Even Thickness spento | Applica la scala; attiva Even Thickness |
| La lastra si sviluppa verso il basso (Z negativa) | Offset -1 con normali verso l'alto | Offset +1 |
| Le copie si sovrappongono o sono troppo lontane | Offset dell'Array relativo, non in mm | Usa la formula (L + G) / L |
| Il modificatore non sembra agire | Pulsante monitor spento, o oggetto sbagliato selezionato | Controlla il monitor e il nome nel pannello |
| Mesh non chiusa dopo i modificatori | Ordine sbagliato o Merge spento | Controlla lo stack: Mirror → Solidify → Array |

## 10. Checklist di verifica

- [ ] Aggiungo Mirror, Solidify e Array da `Add Modifier → Generate`.
- [ ] Metto l'origine sul piano di specchio e cancello la faccia con `X` → Faces.
- [ ] Applico la scala prima dei modificatori.
- [ ] Attivo Even Thickness e imposto lo spessore in mm.
- [ ] Calcolo l'Offset dell'Array con (L + G) / L.
- [ ] Controllo dimensioni finali, copie e mesh chiusa.
- [ ] Spiego **perché** l'ordine dei modificatori conta.

## 11. Domande di ripasso (rispondi con una frase causa → conseguenza)

1. Perché con Mirror si può modellare solo metà oggetto?
2. Perché l'origine deve stare sul piano di specchio?
3. Perché Mirror va **prima** di Solidify?
4. Perché con Scale ≠ 1 le pareti di Solidify non sono quelle che hai scritto?
5. Perché con Merge spento ottieni due corpi?
6. Perché l'Offset dell'Array non è in millimetri?
7. Quando è giusto lasciare le copie dell'Array come corpi separati?

Le risposte sono in `03_soluzioni.md`: leggile **dopo** aver risposto.

## 12. Criteri di valutazione

Vedi `02_esercitazione.md`.
