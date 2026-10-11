# Roadmap

Stato: ⬜ da fare · 🟨 in corso · ✅ superata (con prova pratica)

Nessuna durata è promessa: si avanza quando la prova pratica di ogni fase è superata. La roadmap sarà adattata dopo la Fase 1, quando conosceremo il tuo ritmo.

| Fase | Contenuto | Prova finale | Stato |
|---|---|---|---|
| 0 | Laboratorio: ambiente, Blender installato, cartelle | Blender si avvia e il primo file è salvato | 🟨 |
| 1 | Fondamenti: interfaccia, navigazione, trasformazioni, Edit Mode, extrude/inset/bevel/loop cut, salvataggio | Piccolo oggetto completo, salvato e presentato | ⬜ |
| 2 | Modellazione poligonale: hard surface, Mirror/Array/Solidify/Subdivision, normali, topologia, unità | 3 oggetti di difficoltà crescente a misure reali | ⬜ |
| 3 | Materiali e rendering: PBR, luci a tre punti, HDRI, camera, Cycles/Eevee, denoise | Render di prodotto valutato | ⬜ |
| 4 | Sculpting organico: volumi primari, silhouette, proporzioni, anatomia, dettagli, retopology | Busto/creatura base | ⬜ |
| 5 | Personaggio completo: scheda, riferimenti, blockout, scultura, materiali, presentazione | Personaggio finito | ⬜ |
| 6 | Stampa 3D: FDM vs resina, spessori, manifold, hollowing, incastri, slicer | Miniatura verificata nello slicer | ⬜ |
| 7 | Progetti integrati | Progetto con criteri di accettazione | ⬜ |

## Fase 0 — checklist

- [x] Verificato ambiente di lavoro del tutor (vedi sotto)
- [x] Struttura cartelle creata
- [x] Tuo computer: Windows, Blender **5.0.1**, preferenza Eevee
- [ ] Hardware del tuo computer (RAM, scheda video)
- [ ] Stampante / tecnologia (FDM o resina) — serve dalla Fase 6, non ora
- [ ] Decisione su come usare Blender (vedi `README` / risposta al tutor)

## Capacità reali del tutor in questo ambiente (verificate l'11/10/2026)

| Cosa | Esito |
|---|---|
| Terminale e filesystem | ✅ Linux, 4 core, 15 GB RAM, nessuna GPU |
| Blender | ✅ **5.0.1** (la tua versione) in `/opt/blender-5.0.1`, comando `blender`; in più 5.2.2 LTS come `blender-5.2.2`. Checksum SHA-256 verificati |
| Python | ✅ 3.13 di sistema (numpy, Pillow); Python di Blender 3.13 con API `bpy` funzionante |
| Slicer, MeshLab, FreeCAD | ❌ non installati |
| Aprire/analizzare `.blend` in background | ✅ testato (avvio e API) |
| Render Cycles su CPU | ✅ testato (immagine 320x240 generata) |
| Render **Eevee** in background | ❌ fallisce: manca `libEGL.so.1`. Si risolve installando le librerie grafiche Mesa (chiesta conferma) |

Il tutor lavora su una macchina remota, **diversa dal tuo computer**: non vede il tuo schermo. Per correggerti serve che tu carichi i file (o screenshot) nel repository.

**Compatibilità file:** un `.blend` salvato con una versione più recente (es. 5.2) può non aprirsi bene nella 5.0.1. I file didattici del corso sono sempre generati con la 5.0.1.
