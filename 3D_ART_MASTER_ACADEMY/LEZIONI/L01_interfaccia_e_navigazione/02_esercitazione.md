# Esercitazione L01 — Disporre cinque forme nello spazio

**Livello:** 1 (principiante) · **Tempo indicativo:** 45–60 min per la guidata, 20–30 per l'autonoma
**Strumenti:** Blender 5.0.1, `materiali/L01_start.blend`
**Dispensa di riferimento:** `01_dispensa.md`

Apri `L01_start.blend` e **salvalo subito come `consegne/L01_guidata_v01.blend`** (File → Save As). Non lavorare sull'originale.

Nella scena ci sono cinque oggetti sparsi a terra: **Cubo, Cono, Cilindro, Sfera, Toro** (di default sono tutti dritti, scala 1).

---

## Parte A — Modalità guidata

### A1. Esplora la scena (5 min)
1. Con il mouse sulla viewport usa Orbit, Pan e Zoom per girare attorno agli oggetti.
2. Premi `Home` (o `View → Frame All`) per inquadrare tutto.
3. Vai in vista **Top** (`Numpad 7` o `View → Viewpoint → Top`) e poi **Front** (`Numpad 1` o `View → Viewpoint → Front`).
**Risultato atteso:** in Top vedi cinque forme sparse su un piano; in Front le vedi tutte alla stessa altezza.

### A2. Sposta con valori precisi (15 min)
Per ogni oggetto: cliccalo, premi `N`, scheda **Item** → **Transform**, scrivi i valori in **Location** (usa il punto per i decimali, `Tab` per passare al campo seguente).

| Oggetto | Location X | Location Y | Location Z |
|---|---|---|---|
| Cubo | -4 | 0 | 1 |
| Cono | -2 | 0 | 1 |
| Cilindro | 0 | 0 | 1.5 |
| Sfera | 2 | 0 | 1 |
| Toro | 4 | 0 | 1 |

**Risultato atteso:** in vista Top gli oggetti sono allineati in fila lungo l'asse X (rosso).

### A3. Ruota (10 min)
Con la **sidebar** o con la tastiera:
- **Cono:** `R`, `X`, `180`, `Enter` → capovolto, punta verso il basso.
- **Toro:** `R`, `X`, `90`, `Enter` → in piedi, come una ruota vista di lato.

**Se ruoti dalla parte sbagliata** (cambia solo il segno) il risultato in questa lezione non cambia: va bene.

### A4. Scala (10 min)
Seleziona il **Cilindro**: `S`, `Z`, `1.5`, `Enter` (diventa alto 3 m). Poi `S`, `Shift` + `Z`, `0.5`, `Enter`: scala X e Y insieme, a metà. In Sidebar controlla **Scale = 0.5, 0.5, 1.5**.

> `Shift` + asse significa "tutti gli assi **tranne** quello" (qui X e Y).

### A5. Ordine e salvataggio (5 min)
1. Nell'Outliner verifica che i nomi siano quelli originali (non rinominarli: serve per la verifica).
2. Salva (`Ctrl` + `S`), poi `File → Save As` come `L01_guidata_v02.blend`.
3. Fai un render veloce di controllo: `F12` mostra il risultato (non serve salvarlo).

### Controllo A
Il risultato deve assomigliare a `materiali/L01_A_fronte.png` (vista Front) e `L01_A_alto.png` (vista Top), con Perspective/Orthographic su ortografica.

---

## Parte B — Modalità autonoma (prova di superamento)

**Attenzione:** questa è una disposizione **diversa** dalla Parte A (altro asse, altro ordine, altre altezze e scale). Non puoi ricopiare i numeri della guidata.

**Consegna:** apri di nuovo `L01_start.blend` e salvalo come `consegne/L01_autonoma_v01.blend`. Ricostruisci la disposizione mostrata nelle due immagini:
- `materiali/L01_B_destra.png`: vista **Right** (`Numpad 3` o `View → Viewpoint → Right`), ortografica. A sinistra c'è il Toro, a destra il Cubo.
- `materiali/L01_B_alto.png`: vista **Top** ruotata di 90° (solo per leggere meglio: la fila corre da sinistra a destra).

**Cosa ti dico:**
- gli oggetti sono i cinque di sempre, con i nomi originali;
- sono allineati lungo l'asse **Y** (verde), distanti **2 m** l'uno dall'altro, centrati su Y = 0;
- tutti poggiano sul pavimento (Z = 0) e sono centrati su X = 0;
- l'ordine lungo Y, dal valore più basso al più alto, è quello delle immagini (da sinistra a destra).

**Cosa devi ricavare tu:** posizioni Z e scale (la B non richiede rotazioni: vedi Parte C). Aiutati con la griglia della viewport (1 m per quadretto), con **Dimensions** nella Sidebar e confrontando le vedute.

**Non devi:** rinominare, eliminare o aggiungere oggetti (se ne aggiungi, segnalalo).

**Consegna:** carica nel repository `consegne/L01_autonoma_v01.blend` (e le versioni successive) e scrivimi "consegna L01".

## Parte C — Verifica delle rotazioni (10 min)

La Parte B non usa il comando `R`. Con questa prova breve lo verifichiamo.

1. Apri il file della Parte B che hai consegnato e salvalo come `consegne/L01_rotazioni_v01.blend`.
2. **Cono:** capovolgilo di 180° attorno all'asse X, in modo che la punta guardi in basso. Non cambiare la sua posizione.
3. **Toro:** mettilo "in piedi", come una ruota vista di lato (rotazione di 90° attorno a X), e **alzalo** in modo che poggi sul pavimento (controlla la Location Z da Front).
4. Carica il file in `consegne/` e scrivimi "consegna rotazioni L01". Lo controllo con `script/verifica_L01.py -- C`.

Il tutor non ti dà i valori: ricavali con `R`, l'asse e il numero, oppure dalla Sidebar (Item → Transform → Rotation).

### Criteri di superamento
| Criterio | Peso | Come lo verifico |
|---|---|---|
| Posizioni corrette (tolleranza 15 cm) | 40% | Script `script/verifica_L01.py -- B` (geometria reale) |
| Rotazioni corrette (richieste nella Parte C: nella B nessun oggetto è ruotato) | 25% | Script `-- C` |
| Scale corrette (cilindro) | 15% | Script |
| Scena ordinata (nomi originali, nessun oggetto di troppo) | 10% | Outliner |
| Salvataggio versionato (`_v01`, `_v02`...) | 10% | Nome dei file |

**Condizione per superarla:** 5/5 oggetti corretti **e** almeno 7/10 in totale. Se non la superi, ti dico cosa rivedere e ripeti con una variante.

### Errori da evitare
- Lavorare sul file originale senza salvarlo prima con un altro nome.
- Spostare gli oggetti "a occhio" senza controllare i valori nella Sidebar.
- Confondere la vista: i valori Z si controllano da Front, non da Top.

### Difficoltà
⭐⭐ (due stelle su cinque)
