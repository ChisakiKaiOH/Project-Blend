# Lezione 5 — Soluzioni commentate (leggi solo dopo aver risposto)

## Domande di ripasso

1. Poiché la superficie di Subdivision **approssima** i vertici della gabbia senza toccarli e gli angoli di un cubo si ammorbidiscono verso il centro, il cubo si restringe, quindi le dimensioni passano da 40 a **33,58 mm** per asse e il volume da 64 000 a 19 609 mm³ (31%).
2. Poiché la superficie liscia ha poco spazio tra lo spigolo e l'anello di supporto, il raccordo è breve, quindi più vicino è il supporto più volume resta (supporto a 2 mm: 59 088 mm³; a 6 mm: 56 648 mm³) e le facce tornano a 40 mm.
3. Poiché un Crease 1 dice che lo spigolo non va addolcito, la superficie lo mantiene vivo, quindi il volume resta quello del cubo, **64 000 mm³**, senza arrotondamento.
4. Poiché Shade Smooth modifica solo come viene calcolata la luce sulle facce (proprietà `use_smooth`) e non sposta i vertici, la forma non cambia, quindi dimensioni e volume restano identici.
5. Poiché il modificatore genera 4 volte le facce a ogni livello (6 → 24 → 96 → 384 per un cubo semplice, 480 facce per il blocco con supporti), applicarlo rende la mesh pesante e non più modificabile, quindi non si può più cambiare il raccordo né i livelli.

## Parte A — risposte ai passi
- **A3:** 98 vertici, 96 facce, 33,58 × 33,58 × 33,58 mm.
- **A4:** 32 vertici, 60 spigoli, 30 facce nella base. Sulla copia con Apply: 482 vertici, 480 facce.
- **A5:** 40 × 40 × 40 mm, volume 57 925 mm³ (90,5% del cubo).
- **A6:** supporto a 2 mm → 59 088 mm³; a 6 mm → 56 648 mm³. Con più distanza il raccordo è più largo e il volume scende.
- **A8:** Blocco_crease: base di 8 vertici, 12 spigoli con crease 0,5, volume 58 619 mm³ (91,6%), dimensioni 40 mm.

## Parte B — il sapone (una soluzione possibile)
Il metodo non è unico: lo script misura il risultato. Quella di riferimento (16/16):
1. Cubo 80 × 50 × 20, Apply Scale, Location (0, 0, 10), nome **Sapone**.
2. Face mode, tutte le facce, **Inset 3 mm con Individual** (supporti dei bordi esterni).
3. Sulla faccia superiore interna (74 × 44 mm): **Inset 10,5** poi **Inset 1,5** (→ rettangolo 50 × 20 mm).
4. **Extrude** verso il basso di **1,5 mm** (`E`, `-1.5`).
5. **Inset 1,5** sul fondo (supporto del fondo).
6. Subdivision Viewport 2 / Render 3, Shade Smooth.

Base finale: 48 vertici, 92 spigoli, 46 facce. Misure risultanti: 80 × 50 × 20 mm, volume 72 264 mm³, fondo a Z = 18,5, 736 facce valutate (mesh chiusa, 1 corpo).
Una variante con Crease sui bordi esterni (0,5) e supporti solo sull'incavo è accettata se rispetta i requisiti.

**Errore tipico (verificato con lo script):** incavo senza supporto sul fondo e intorno al bordo → a 3 mm dentro il bordo la superficie sale a Z = 19,0 e a 1–3 mm fuori resta a 19,89: il bordo risulta sfumato e il controllo 10 non passa.

## Parte C — risposte alla diagnosi (leggi solo dopo aver risposto)

| Oggetto | Difetto | Come si riconosce | Perché succede | Correzione |
|---|---|---|---|---|
| **Blocco_1** | **Nessun supporto** | Base di 8 vertici e 6 facce; sulla copia con Apply **98 vertici, 96 facce** e dimensioni **33,58 mm**; forma simile a una sfera | Poiché la superficie approssima i vertici e gli spigoli non hanno supporti, il cubo si restringe a 33,58 mm, quindi le dimensioni finali sono sbagliate e il volume è 19 609 mm³ | Edit Mode, tutte le facce, `I` con **Individual** (es. 4 mm); oppure Crease 0,5 su tutti gli spigoli |
| **Blocco_2** | **Crease troppo forte** (1,0 su tutti gli spigoli) | Overlays → Crease: tutti gli spigoli rossi; la forma ha spigoli vivi nonostante Subdivision; volume 64 000 mm³ | Poiché il crease 1 impedisce l'addolcimento dello spigolo, la superficie mantiene l'angolo vivo, quindi non c'è raccordo (volume 100% del cubo, fuori dalla finestra) | Edge mode, tutti gli spigoli, `Shift` + `E` con valore `-1` (verificato: porta il crease a 0) |
| **Blocco_3** | **Ombreggiatura Flat** | Dimensioni e volume giusti (40 mm, 57 925 mm³), ma la superficie mostra sfaccettature; menu Object: le facce non sono Smooth | Poiché con Flat ogni faccia valutata ha un solo colore di luce, si vedono le 480 sfaccettature, quindi la superficie appare spezzata anche se la geometria è corretta | Object Mode → **Object → Shade Smooth** |

**Riparazione attesa:** tre blocchi 40 × 40 × 40 mm, chiusi, base solo quad, Subdivision livello 2 attivo, Smooth, volume nella finestra 55 000–60 200 mm³ (valore di riferimento: 57 925).

**Nota sul Crease:** verificato su Blocco_2: `Shift` + `E` con `-1` su tutti gli spigoli porta il crease a 0; in alternativa puoi impostare un valore più basso (es. `0.5`). Conta il volume finale.
