# Lezione 5 — Subdivision Surface e controllo degli spigoli

**Livello:** 3 · **Fase 2 (Modellazione poligonale)** · **Blender 5.0.1** · comandi in inglese
**Prerequisiti:** L02 (Inset, Loop Cut), L04 (modificatori, controllo su una copia)

---

## 1. Obiettivi

Alla fine saprai:
1. aggiungere **Subdivision Surface** e scegliere i livelli per Viewport e Render;
2. spiegare perché un cubo con Subdivision diventa una palla e **quanto** si restringe;
3. mantenere gli spigoli con gli **anelli di supporto** (Inset) e con il **Crease** (`Shift`+`E`);
4. dare l'ombreggiatura **Smooth** e sapere perché serve;
5. verificare il risultato con numeri, su una copia.

**Perché serve per SH-Print:** tutti i personaggi organici (L17 in poi) partono da una mesh semplice a quad più Subdivision. Gli spigoli di un oggetto stampato non sono mai perfettamente vivi: avere il controllo del raggio di raccordo serve anche per la resistenza e per la resa in resina.

---

## 2. Concetti base

- **Subdivision Surface** (algoritmo Catmull-Clark) è un modificatore che **divide ogni quad in 4** e poi **sposta i vertici** per addolcire la forma. Non è un "arrotondamento di spigoli": è una superficie liscia **controllata** dalla mesh di partenza (la *gabbia*).
- La superficie liscia **non passa per i vertici della gabbia**: li "approssima", si avvicina senza toccarli (salvo che gli spigoli siano irrigiditi, vedi 5 e 6). Per questo la forma si **restringe**.
- **Livelli (Levels):** quante volte si ripete la divisione. Ogni livello moltiplica le facce per 4.
- Il modificatore è **non distruttivo**, come in L04: la mesh di base resta piccola e modificabile.

### 2.1 Aggiungerlo
- `Add Modifier → Generate → Subdivision Surface`, oppure con l'oggetto selezionato `Ctrl` + `1…5`: imposta quel livello e **aggiunge il modificatore se manca** (`Ctrl` + `0` = livello 0).
- Valori predefiniti verificati sulla 5.0.1: **Levels Viewport 1**, **Render 2**.
- **Levels Viewport** = quello che vedi mentre lavori; **Render** = quello usato nel render finale. Nelle esercitazioni del corso: **Viewport 2, Render 3**.
- Nel pannello i due campi sono **Levels** (Viewport) e **Render**; c'è anche **Optimal Display** (mostra solo gli spigoli della gabbia, non cambia la forma). Per ora non toccare le impostazioni avanzate.

### 2.2 Numeri misurati: un cubo da 40 mm
Misurati con uno script sulla mesh dopo il modificatore (il modificatore si valuta, non si applica):

| Levels | Vertici | Facce | Dimensioni | Volume (mm³) | % del cubo (64 000) |
|---|---|---|---|---|---|
| 0 (spento) | 8 | 6 | 40 × 40 × 40 | 64 000 | 100% |
| 1 | 26 | 24 | 33,58 × 33,58 × 33,58 | 16 151 | 25% |
| 2 | 98 | 96 | 33,58 × 33,58 × 33,58 | 19 609 | 31% |
| 3 | 386 | 384 | 33,58 × 33,58 × 33,58 | 20 615 | 32% |

**Cosa si legge:**
- ogni livello **quadruplica le facce** (24 → 96 → 384);
- le dimensioni non cambiano dopo il livello 1: sono quelle della **superficie limite**; salgono solo morbidezza e numero di facce;
- un cubo diventa una forma simile a una sfera e perde **circa il 70% del volume**: se vuoi uno spigolo che **resti** nella posizione voluta, devi controllarlo.

---

## 3. Come misurare il risultato (sulla copia, come in L04)

Con il modificatore attivo, la mesh che vedi è quella valutata, ma i numeri nei pannelli possono riferirsi alla mesh di base (non l'ho verificato sulla tua schermata). Metodo sicuro:
1. `Shift` + `D`, clic destro (copia);
2. sulla copia: menu del modificatore → **Apply**;
3. `N` → Item → **Dimensions**; Overlays → **Statistics** per vertici e facce;
4. elimina la copia (`X`).

Nella copia con Levels 2 dal cubo semplice troverai **98 vertici e 96 facce** (stessi numeri della tabella).

---

## 4. Perché i bordi si arrotondano: la regola dei supporti

Un modificatore Subdivision addolcisce ogni spigolo **in proporzione alla distanza** tra gli spigoli vicini. Se aggiungi un anello di spigoli **vicino** a uno spigolo vivo (un *anello di supporto*, *support loop*), la superficie ha poco spazio per arrotondare e lo spigolo resta **più netto**. Più è vicino il supporto, più è netto.

### 4.1 Come creare i supporti: Inset individuale
1. Edit Mode, modo **Face**, `A` (tutte le facce).
2. `I`, scrivi `4`, `Enter`.
3. Nel pannello in basso a sinistra (**Inset Faces**) attiva **Individual**. Così ogni faccia ottiene la sua cornice a 4 mm dai bordi.
4. Controlla la mesh di base: ora ha **32 vertici, 60 spigoli, 30 facce** (cubo da 40).

**Importante:** con **Individual** spento, `I` tratta tutte le facce selezionate come un'unica regione e inserisce la cornice solo sul suo **contorno**. Un cubo chiuso con tutte le facce selezionate non ha contorno: verificato, la mesh resta di **8 vertici e 6 facce** e non succede nulla.

Alternativa: `Ctrl` + `R` (Loop Cut) vicino ai bordi, con 1 taglio e poi spostamento preciso con `G`, `G` (Edge Slide). È più lunga ma più flessibile per forme non cubiche.

### 4.2 Numeri misurati: cubo 40 mm, Levels 2, supporti a distanza diversa
| Supporto a | Dimensioni | Volume (mm³) | % del cubo |
|---|---|---|---|
| nessuno | 33,58³ | 19 609 | 31% |
| 6 mm | 40 × 40 × 40 | 56 648 | 88,5% |
| 4 mm | 40 × 40 × 40 | 57 925 | 90,5% |
| 2 mm | 40 × 40 × 40 | 59 088 | 92,3% |

**Cosa si legge:** bastano i supporti per recuperare **le dimensioni intere** (le facce tornano piatte), e più il supporto è vicino, più volume resta (spigolo più vivo). Il **raggio dello spigolo** lo scegli tu con la distanza del supporto.

---

## 5. Crease: irrigidire gli spigoli senza aggiungere geometria

Il **Crease** è un valore da 0 a 1 assegnato a uno **spigolo**: dice quanto quello spigolo deve restare vivo.
1. Edit Mode, modo **Edge**, seleziona gli spigoli.
2. `Shift` + `E`, scrivi il valore (es. `0.5`), `Enter`.
3. Per **vedere** i crease: Overlays (nell'Edit Mode) → casella **Crease**.

**Numeri misurati (cubo semplice da 40 mm, Levels 2, crease uguale su tutti i 12 spigoli):**

| Crease | Dimensioni | Volume (mm³) | % del cubo |
|---|---|---|---|
| 0 | 33,58³ | 19 609 | 31% |
| 0,25 | 37,59³ | 35 237 | 55% |
| 0,5 | 40³ | 58 619 | 91,6% |
| 0,75 | 40³ | 60 359 | 94,3% |
| 1 | 40³ | 64 000 | 100% (cubo con facce, ma nessun arrotondamento) |

**Cosa si legge:** il Crease 1 annulla del tutto l'arrotondamento; **il valore efficace dipende dai Levels** (ogni livello "consuma" parte del crease). Con Levels 2, circa 0,5 produce un raccordo come un supporto a 4 mm. Se cambi i livelli, cambia il risultato: ricontrolla.

### 5.1 Supporti o Crease?
| | Supporti (Inset/Loop Cut) | Crease |
|---|---|---|
| Geometria | più facce nella base | base minima |
| Controllo | preciso e visibile nella mesh | un solo numero per spigolo |
| Uso tipico | forme da modificare ancora, bordi con forme complesse | blocchi semplici, hard surface rapido |

Non c'è un metodo "giusto": il controllo dice se il **risultato** è corretto.

---

## 6. Regole d'oro per la base

1. **Solo quad** nella mesh di base. Triangoli e n-gon (facce con più di 4 lati) possono far "pizzicare" la superficie vicino al punto in cui si incontrano; la teoria completa e le misure arrivano in L07. Per ora la regola è: **solo quad**, e lo script lo controlla.
2. **Scale = 1** (come per tutti i modificatori della L04).
3. **Origine e posizione** come specificato (qui: l'oggetto poggia sul pavimento).
4. **Subdivision non si applica** in questa lezione (Apply è nella L08).

---

## 7. Shade Smooth

Con Subdivision, la mesh valutata ha tante piccole facce: se l'ombreggiatura è **Flat**, ogni faccia ha un colore uniforme e si vede la **sfaccettatura**; con **Smooth** il colore varia con continuità sui vertici.
- Object Mode, oggetto selezionato: menu **Object → Shade Smooth** (o tasto destro nella viewport → Shade Smooth).
- Per tornare indietro: **Shade Flat**.
- È una proprietà delle facce della mesh (nella 5.0.1 verificata con `use_smooth`), non del modificatore: va impostata sull'oggetto.
- **Non cambia la forma**: le dimensioni e il volume restano uguali; cambia solo come viene calcolata la luce. L'approfondimento sulle normali è nella L06.

---

## 8. Ordine nello stack

Se l'oggetto ha già altri modificatori (Mirror, Solidify, Array...), **Subdivision Surface va dopo** i modificatori che costruiscono la forma. Per ora, nelle esercitazioni, è l'unico modificatore.

---

## 9. Procedura tipica

1. Modella la base con pochi quad e le dimensioni reali.
2. `Apply Scale` (Scale 1).
3. Aggiungi Subdivision: Viewport 2, Render 3.
4. Controlla il risultato sulla **copia** (dimensioni, statistiche).
5. Aggiungi supporti o Crease dove serve uno spigolo netto.
6. Shade Smooth.
7. Controlla di nuovo: nomi, collezione, scala, mesh chiusa.

---

## 10. Errori frequenti

| Errore | Conseguenza | Come riconoscerlo |
|---|---|---|
| Nessun supporto | forma gonfia, dimensioni ridotte del 16% (40 → 33,58) | volume al 31% |
| Crease 1 su tutto | nessun arrotondamento | volume 100% |
| Flat Shading | sfaccettature visibili | aspetto "a gradini" sulle facce valutate |
| Applicare il modificatore per errore | base da centinaia di facce, non modificabile | vertici della base molto alti |
| Triangoli o n-gon nella base | pizzichi sulla superficie | controllo "solo quad" |
| Scale diversa da 1 | supporti e raggi non uniformi | `N` → Scale |

---

## 11. Checklist di verifica (usala prima di consegnare)

- [ ] **Nome** dell'oggetto esattamente come richiesto (maiuscole comprese)
- [ ] Oggetto nella collezione **Modello**, nessun oggetto fuori dalle collezioni
- [ ] **Scale 1**, rotazione 0
- [ ] **Un solo** modificatore Subdivision Surface, **Viewport 2, Render 3**, non applicato
- [ ] Mesh di base **solo quad**
- [ ] **Shade Smooth** su tutte le facce
- [ ] Dimensioni finali giuste (misurate su una copia)
- [ ] Il file salvato con il nome versionato giusto, in `consegne/`

---

## 12. Domande di ripasso

(Rispondi con una frase "Poiché [cosa succede nel programma], [effetto], quindi [conseguenza misurabile]".)

1. Perché un cubo con Subdivision Surface e senza supporti ha dimensioni più piccole di quelle di partenza?
2. Perché un anello di supporto vicino allo spigolo lo rende più netto?
3. Perché con Crease 1 il cubo non si arrotonda?
4. Perché Shade Smooth non cambia le dimensioni dell'oggetto?
5. Perché non conviene applicare Subdivision mentre si modella?

---

## 13. Criteri di valutazione

| Parte | Peso | Come |
|---|---|---|
| A guidata | controlli automatici | `script/verifica_L05.py -- A` |
| B autonoma (prova di superamento) | controlli automatici, **16/16** | `script/verifica_L05.py -- B` |
| C riparazione | controlli automatici 3/3 e diagnosi scritta | `script/verifica_L05_C.py` |

Il voto della lezione si calcola come nelle precedenti: ogni punto perso ha un motivo verificabile.
