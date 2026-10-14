# Lezione 4 — Soluzioni commentate (leggi solo dopo aver risposto)

1. Perché la forma è **simmetrica**: la seconda metà è il riflesso della prima rispetto a un piano, quindi basta modellarne una e il Mirror produce l'altra; se cambi la metà, cambia anche l'intero.
2. Perché Mirror riflette rispetto al piano che passa per l'**origine** dell'oggetto: se l'origine è fuori dal piano di specchio, le due metà non si toccano e non si uniscono (due corpi o un vuoto al centro).
3. Perché ogni modificatore lavora sul risultato del precedente. Con Mirror **prima**, Solidify dà spessore all'oggetto intero già completo. Con Solidify **prima**, dà spessore alla sola metà e chiude anche il bordo sul piano di specchio: dopo il Mirror la mesh non risulta chiusa (misurato: 8 spigoli non-manifold).
4. Perché lo spessore di Solidify è espresso nelle unità dell'oggetto e si moltiplica per la scala: con Scale 0.5 e Thickness 2, le pareti sono di 1 mm (volume 8864 mm³ invece di 17072). Si applica la scala prima.
5. Perché Merge Vertices fonde i vertici che coincidono sul piano di specchio; con Merge spento restano due serie di vertici sovrapposte, quindi due corpi separati e vertici doppi (misurato: 2 corpi, 8 vertici doppi).
6. Perché l'Offset dell'Array nel modo Relative si misura in multipli della dimensione dell'oggetto in input: `1` significa "una larghezza", quindi una distanza in mm si ottiene con (L + G) / L.
7. Quando le copie sono pezzi indipendenti da stampare nello stesso lavoro (piatto di stampa) e restano separate da un vuoto sufficiente; sono ognuna una mesh chiusa. Se dovessero formare un unico pezzo, servirebbe un'unione.

## Parte A, passo A6 — risposta all'esperimento
Con Solidify sopra Mirror la mesh diventa non chiusa: sulla **copia con i modificatori applicati** la vaschetta singola ha **8 spigoli non-manifold** (24 vertici, 46 spigoli, 25 facce); nella versione con 3 copie sono 24. Il difetto nasce perché Solidify ha già chiuso il bordo sul piano di specchio prima che il Mirror duplichi la metà.

## Parte C — risposte alla diagnosi (leggi solo dopo aver risposto)

| Oggetto | Difetto | Come si riconosce | Perché succede | Correzione |
|---|---|---|---|---|
| **Vaschetta_1** | **Ordine dei modificatori sbagliato** (Solidify sopra Mirror) | Nel pannello l'ordine è Solidify → Mirror; sulla **copia con modificatori applicati** Non Manifold seleziona **8 spigoli** (46 spigoli e 25 facce in totale) | Solidify chiude il bordo sul piano di specchio prima che il Mirror duplichi la metà, quindi il risultato non è un solido chiuso | Trascina Mirror sopra Solidify, oppure Solidify → menu → Move to Last |
| **Vaschetta_2** | **Scala non applicata** (Scale 0.5, mesh dilatata) | In `N` Scale = 0.5, 0.5, 0.5; Dimensions sono giuste (80 × 50 × 20) e anche i conteggi sulla copia sono giusti (24/44/22), ma le pareti sono sottili (1 mm): è l'unico difetto che i conteggi **non** rivelano | Thickness si moltiplica per la scala dell'oggetto: 2 × 0.5 = 1 mm reale | Object Mode: `Ctrl` + `A` → Scale, poi Scale = 1 e pareti da 2 mm |
| **Vaschetta_3** | **Merge Vertices spento** nel Mirror | Il risultato sembra intero, ma la copia con modificatori applicati ha **32 vertici invece di 24**; Merge By Distance ne rimuove **8** | Senza Merge le due metà restano separate, con vertici sovrapposti | Attiva Merge Vertices nel Mirror |

**Riparazione attesa:** tre vaschette 80 × 50 × 20 mm, chiuse, un corpo, nessun vertice doppio, volume 17072 mm³, stack Mirror → Solidify, Scale 1.
