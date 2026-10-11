# Lezione 2 — Soluzioni commentate (leggi solo dopo aver risposto)

1. In **Object Mode** sposti, ruoti e scali l'oggetto intero. In **Edit Mode** modifichi la sua forma: vertici, spigoli e facce.
2. Una mesh è *manifold* (chiusa) quando non ha buchi e ogni spigolo appartiene a **due** facce. Per stampare serve perché lo slicer deve capire che cosa è "dentro" e che cosa è "fuori" il solido: un buco o una faccia interna rende ambiguo il volume.
3. **Inset** (e in modo analogo i valori che dipendono dallo spazio dell'oggetto) viene moltiplicato per la scala: con Scale 0.15 un inset di 0.1 dà 0.015 m reali (verificato su Blender 5.0.1). L'estrusione, invece, usa le misure reali. Per evitare ambiguità si applica sempre la scala (`Ctrl` + `A` → Scale) prima di modellare.
4. In Edit Mode: `Ctrl` + `R`, rotella per portare i tagli a **2**, clic sinistro per confermare, **clic destro** per lasciarli equidistanti (3 parti uguali).
5. **Dissolve** (`Ctrl` + `X`): ricuce la geometria. **Delete → Faces** lascia un buco.
6. Rossa = la normale punta verso l'interno. In Edit Mode: seleziona tutto con `A`, poi `Mesh → Normals → Recalculate Outside` (`Shift` + `N`). Se serve invertire solo certe facce: `Mesh → Normals → Flip`.
7. Perché sono 5 corpi distinti che si toccano senza essere fusi: la stampa richiede un solo volume chiuso (o un'unione precisa). L'estrusione dalle facce del piano produce un solo corpo.

## Parte C — risposte alla diagnosi (leggi solo dopo aver risposto)

| Domanda | Risposta |
|---|---|
| Statistics con niente selezionato | **10 vertici, 12 spigoli, 5 facce** |
| Facce che avrebbe un cubo chiuso | **6**: manca la faccia **superiore** |
| Select All by Trait → Loose Geometry | **2 vertici** selezionati |
| Face Orientation: faccia rossa | La faccia **frontale** (quella che vedi in vista Front, `Numpad 1`) |
| Perché Non Manifold seleziona più di 4 spigoli | Oltre ai 4 spigoli del buco superiore si illuminano anche quelli della faccia rossa: la sua normale è invertita, quindi i bordi con le facce vicine sono incoerenti |
| Può essere stampato? | **No**: ha un buco, due vertici sciolti e una faccia con normale invertita |

**Riparazione attesa:** cancella i 2 vertici sciolti (Select → Select All by Trait → Loose Geometry → `X` → Vertices), seleziona i 4 vertici del bordo del buco e premi `F`, poi `A` e `Shift` + `N`. Risultato: **8 vertici, 12 spigoli, 6 facce**, chiuso, normali verso l'esterno.
