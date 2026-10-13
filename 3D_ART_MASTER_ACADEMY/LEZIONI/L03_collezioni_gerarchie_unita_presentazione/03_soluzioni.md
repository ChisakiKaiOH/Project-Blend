# Lezione 3 — Soluzioni commentate (leggi solo dopo aver risposto)

1. La **collezione** ordina e permette di nascondere gruppi di oggetti, ma gli oggetti restano indipendenti. La **gerarchia** (parent) lega gli oggetti: muovendo il genitore, i figli lo seguono.
2. Un **Empty** non ha geometria: è un punto di riferimento che non si vede nel render e non interferisce con il modello. Posizionato a terra al centro della base, diventa il "punto di appoggio" dell'intero gruppo.
3. **Keep Transform** conserva la posizione che i figli hanno **in questo momento** nello spazio: senza, al collegamento potrebbero spostarsi.
4. **Unit Scale 0.001** significa che 1 unità Blender vale 1 mm. Se lo imposti dopo aver modellato, i numeri già inseriti cambiano significato: un oggetto di 2 BU, prima "2 m", diventa "2 mm". Si imposta prima di modellare.
5. Perché non dicono cosa sono e non si possono ritrovare. In una scena con decine di parti, perdi tempo e fai errori. Inoltre gli script di controllo si basano sui nomi.
6. Il `.blend` salva la scena, non l'immagine renderizzata: il PNG è un file a parte (`Image → Save As` nella finestra Render Result).
7. Puoi tornare a una versione precedente se sbagli, e hai la cronologia del lavoro.

## Parte C — risposte alla diagnosi (leggi solo dopo aver risposto)

| Oggetto | Statistics (totali) | Non Manifold | Face Orientation | Difetto | Riparazione |
|---|---|---|---|---|---|
| **Oggetto_A** | 8 vertici, 12 spigoli, 6 facce (**come un cubo normale**) | **nulla selezionato** | **tutte le facce rosse** | **Normali invertite** su tutta la mesh (volume negativo) | In Edit Mode: `A`, poi `Shift` + `N` (Recalculate Outside) |
| **Oggetto_B** | 12 vertici, 20 spigoli, **11 facce** (un cubo chiuso ha 6, qui ce ne sono 11) | **4 spigoli** selezionati (e 1 faccia) | tutte blu | Una **faccia interna** che divide il solido in due: 4 spigoli sono condivisi da 3 facce (non-manifold) | Seleziona la faccia con `Select → Select All by Trait → Interior Faces`, poi `X` → **Faces** |
| **Oggetto_C** | **24 vertici**, 24 spigoli, 6 facce (un cubo ne ha 8) | **tutti i 24 spigoli** selezionati | tutte blu | **Vertici doppi**: le 6 facce sono separate, ogni spigolo è di una sola faccia (bordo) | Edit Mode: `A`, poi `M` → **By Distance** (rimuove 16 vertici) |

**Punto chiave sull'Oggetto_A:** Statistics e Non Manifold **non lo rivelano**. Si vede solo con **Face Orientation** (tutto rosso). Per questo il controllo delle normali è un passo separato.

**Perché nessuno dei tre si stampa correttamente:**
- A: le normali puntano all'interno, quindi lo slicer scambia dentro e fuori;
- B: ha una faccia interna, cioè non è un unico volume pulito;
- C: non è un solido chiuso, ma sei facce separate; non c'è un volume continuo.

**Riparazione attesa:** tre mesh chiuse, un solo corpo, normali verso l'esterno, nessun vertice doppio, volume ≈ 8000 mm³ ciascuna.
