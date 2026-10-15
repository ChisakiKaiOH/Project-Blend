# L05 Parte B — Traccia passo-passo del Sapone (da stampare)

**Sequenza provata da me con i comandi di Blender 5.0.1: porta a 16/16.** Ogni passo ha un valore da controllare: se non coincide, **fermati** e scrivimi il numero del passo e cosa vedi. Segui l'ordine: cambiarlo cambia i risultati.
Parti da `materiali/L05_obiettivo_B.blend` e salvalo come `consegne/L05_autonoma_v04.blend`. Il tuo oggetto ha un solo scopo: assomigliare a `Obiettivo_Sapone` (verde, X = 120).

| ☐ | Passo | Deve risultare |
|---|---|---|
| ☐ | **1.** Clic sulla collezione **Modello**. `Shift`+`C`. `Add → Mesh → Cube` | Cubo dentro Modello |
| ☐ | **2.** `N` → Dimensions `80`, `50`, `20`. `Ctrl`+`A` → **Scale** | Scale 1,1,1 |
| ☐ | **3.** Location `0`, `0`, `10`. `F2` → nome **Sapone** | Poggia sul pavimento, nome esatto |
| ☐ | **4.** `Tab`, modo **Face** (`3`), `A` (tutte). `I`, digita `3`, `Enter`. Nel pannello **Inset Faces** spunta **Individual** | Statistics: **32 vertici, 60 spigoli, 30 facce** |
| ☐ | **5.** Deseleziona (`Alt`+`A`). Clic sul **centro della faccia superiore** (la grande, 74 × 44 mm) | Statistics: **Faces 1/30**; `N` → Median Z Global = 20 |
| ☐ | **6.** `I`, digita `10.5`, `Enter`. Poi di nuovo `I`, digita `1.5`, `Enter` (nel pannello Individual non serve) | La faccia selezionata è un rettangolo **50 × 20** (verifica: clicca un suo vertice → `N` → Vertex Global: X = ±25, Y = ±10) |
| ☐ | **7.** `E`, digita `-1.5`, `Enter` (extrude verso il basso) | Faccia selezionata a **Z Global = 18,5** |
| ☐ | **8.** `I`, digita `1.5`, `Enter` (supporto sul fondo) | Statistics: **48 vertici, 92 spigoli, 46 facce** |
| ☐ | **9.** `Tab`. Properties → **Modifiers** → `Add Modifier → Generate → Subdivision Surface`: **Levels Viewport** `2`, **Render** `3` | Sapone arrotondato con incavo |
| ☐ | **10.** Menu **Object → Shade Smooth** | Niente sfaccettature |
| ☐ | **11.** Confronto con `Obiettivo_Sapone` in vista Top e Right (ortografica) | Stessa forma |
| ☐ | **12.** Elimina la collezione **Obiettivo** (e l'oggetto dentro). Salva `L05_autonoma_v04.blend` | Nel file: solo Camera, Sole, Pavimento, Sapone |

## Perché funziona (da ricordare per la frase finale)
- **Passo 4:** l'Inset **Individual** crea un anello di supporto a 3 mm su **tutti e 12** gli spigoli esterni: le facce restano piatte e le dimensioni finali tornano 80 × 50 × 20.
- **Passo 6:** i due Inset portano il contorno dell'incavo a 50 × 20 mm con un anello piatto di 1,5 mm intorno: lo spigolo del bordo resta netto.
- **Passo 7:** l'Extrude crea **pareti verticali** (non inclinate) profonde 1,5 mm.
- **Passo 8:** senza l'anello sul fondo, lo spigolo tra parete e fondo si arrotonda e l'incavo si sfuma.

## Errori da non rifare (dalle tue v02 e v03)
- ☐ Non applicare **Subdivision** (Apply): resta attivo nel pannello Modifiers.
- ☐ Non usare Crease a valori diversi (0,5, 0,89, 0,99) su tanti spigoli: qui non servono.
- ☐ Spuntare **Individual** al passo 4 (senza, `I` non fa nulla su tutte le facce).
- ☐ **Shade Smooth** su Sapone (Object Mode).
