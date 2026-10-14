# Glossario

Si aggiorna a ogni lezione. Ordine alfabetico.

| Termine | Definizione semplice |
|---|---|
| Blender | Programma gratuito e open source per modellare, scolpire, animare e fare render in 3D. |
| Mesh | La "superficie" di un oggetto 3D, fatta di vertici, spigoli e facce. |
| Vertice | Un punto nello spazio 3D. |
| Spigolo (edge) | Segmento che unisce due vertici. |
| Faccia (face) | Superficie chiusa da spigoli (di solito 3 o 4 lati). |
| Viewport | La finestra 3D di Blender in cui vedi e lavori sul modello. |
| Asse X / Y / Z | Le tre direzioni dello spazio 3D. In Blender Z è l'alto. Colori: X rosso, Y verde, Z blu. |
| Object Mode | Modalità in cui lavori sugli oggetti interi (non sui singoli vertici). |
| Origine (Origin) | Il puntino arancione di un oggetto: il suo punto di riferimento. La Location è la posizione dell'origine. |
| Location / Rotation / Scale | Posizione, rotazione (in gradi) e dimensione di un oggetto. |
| Orbit / Pan / Zoom | Ruotare la vista / spostare la vista / avvicinare-allontanare. Non muovono gli oggetti. |
| Prospettica / Ortografica | Con la prospettiva gli oggetti lontani sembrano più piccoli; in ortografica no, quindi le misure sono confrontabili. |
| Outliner | Elenco di tutti gli oggetti della scena. |
| Properties | Pannello con le impostazioni dell'oggetto selezionato, materiali e render. |
| Sidebar (N) | Pannello della viewport con i valori numerici precisi (scheda Item → Transform). |
| 3D Cursor | Il mirino rosso/bianco: dove compaiono i nuovi oggetti. `Shift+C` lo riporta al centro. |
| Oggetto attivo | L'unico oggetto "principale" della selezione (contorno arancione chiaro). |
| Gizmo di navigazione | Widget in alto a destra nella viewport per ruotare, spostare e zoomare con il mouse, senza tastierino. |
| Edit Mode | Modalità in cui modifichi la forma di un oggetto: vertici, spigoli e facce. |
| Extrude | Crea nuova geometria "tirando" una faccia, uno spigolo o un vertice (tasto `E`). |
| Inset | Crea dentro una faccia una faccia più piccola, circondata da una cornice (tasto `I`). |
| Loop Cut | Aggiunge un anello di spigoli che gira attorno alla mesh (`Ctrl+R`). |
| Bevel | Smussa uno spigolo vivo con una piccola faccia inclinata (`Ctrl+B`). |
| Apply Scale | Rende Scale = 1 senza cambiare la forma visibile (`Ctrl+A` → Scale). Serve prima di Inset, Bevel e modificatori. |
| Normale | La direzione "verso l'esterno" di una faccia. Se è invertita, la faccia guarda all'interno. |
| Mesh chiusa (manifold) | Mesh senza buchi, in cui ogni spigolo appartiene a due facce. Requisito base per la stampa. |
| Non-manifold | Mesh con buchi, facce interne, spigoli condivisi da 3 o più facce, o parti sciolte. |
| Shell (corpo) | Un pezzo di mesh connesso. Un tavolo in un solo pezzo ha 1 shell. |
| Vertici doppi | Due o più vertici nello stesso punto. Si fondono con `M` → By Distance. |
| Collezione (Collection) | "Cartella" della scena per organizzare gli oggetti. Non lega gli oggetti tra loro. |
| Gerarchia (parent / figli) | Legame tra oggetti: muovendo il genitore, i figli lo seguono. |
| Empty | Oggetto senza geometria, usato come punto di riferimento (spesso come root di un gruppo). |
| Keep Transform | Opzione del parenting: i figli non cambiano posizione al momento del collegamento. |
| Unità Blender (BU) | Unità interna di Blender. Con Unit Scale 0.001, 1 BU = 1 mm. |
| Unit Scale | Fattore che trasforma le BU in metri. 0.001 = lavorare in millimetri. |
| Immagine di riferimento | Empty con un'immagine, usato come guida per modellare. Non compare nel render. |
| Modificatore (modifier) | Operazione applicata a una mesh senza cambiare i suoi vertici originali (non distruttiva). |
| Stack dei modificatori | Elenco dei modificatori di un oggetto, calcolati dall'alto verso il basso: l'ordine conta. |
| Apply (modificatore) | Trasforma il risultato di un modificatore in geometria vera e lo toglie dallo stack. Irreversibile. |
| Mirror | Modificatore che riflette la mesh rispetto a un piano passante per l'origine: si modella solo metà. |
| Solidify | Modificatore che dà spessore a una superficie. Richiede Scale 1, Even Thickness e un Offset adatto alle normali. |
| Even Thickness | Opzione di Solidify che mantiene costante lo spessore negli angoli. |
| Array | Modificatore che crea copie a distanza regolare. Nel modo Relative l'Offset è un multiplo della dimensione dell'oggetto. |
| Subdivision Surface | Modificatore che divide ogni quad in 4 e addolcisce la forma. La superficie liscia approssima la gabbia (non passa per i suoi vertici). |
| Gabbia (cage) | La mesh di base, a pochi quad, che controlla la superficie liscia. |
| Levels Viewport / Render | Quante volte Subdivision divide la mesh: uno per la vista di lavoro, uno per il render. Ogni livello quadruplica le facce. |
| Anello di supporto (support loop) | Anello di spigoli vicino a uno spigolo vivo: lo mantiene netto sotto Subdivision. Più è vicino, più lo spigolo è netto. |
| Inset Individual | Opzione di Inset che dà una cornice a ogni faccia separatamente: crea supporti su tutti gli spigoli di un cubo chiuso. |
| Crease | Valore 0–1 su uno spigolo (`Shift`+`E`): 1 lo mantiene vivo sotto Subdivision. L'effetto dipende dai Levels. |
| Shade Smooth / Shade Flat | Ombreggiatura delle facce: Smooth fa variare la luce con continuità, Flat dà un colore per faccia. Non cambia la forma. |
