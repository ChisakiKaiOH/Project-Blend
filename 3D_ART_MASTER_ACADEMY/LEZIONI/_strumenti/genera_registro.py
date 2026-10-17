#!/usr/bin/env python3
"""Genera il registro (REGISTRO.md) e le schede stampabili per lezione (scheda_registro_LXX.md) dai dati in DATI.
Uso (dalla cartella 3D_ART_MASTER_ACADEMY):  python3 LEZIONI/_strumenti/genera_registro.py
Poi:  bash LEZIONI/_strumenti/crea_pdf.sh REGISTRO.md LEZIONI/*/scheda_registro_*.md
Per aggiornare dopo una lezione: modifica DATI (stato, data, esiti, voto) e rilancia.
"""
import os, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AGGIORNATO = "2026-10-17"

DATI = {
 "blocchi": [
  {"n": 1, "nome": "Fondamenti", "lezioni": ["L01", "L02", "L03"], "prova": "Piccolo oggetto completo, salvato e presentato (casetta)"},
  {"n": 2, "nome": "Modellazione poligonale (in corso)", "lezioni": ["L04", "L05"], "prova": "3 oggetti a misure reali (prova finale del blocco: più avanti)"},
 ],
 "lezioni": {
  "L01": {"titolo": "Interfaccia e navigazione", "cartella": "L01_interfaccia_e_navigazione", "data": "2026-10-11", "stato": "Completata", "voto": "10/10",
   "argomenti": ["Interfaccia di Blender, viewport, Outliner, Properties", "Orbit, Pan, Zoom; viste ortografiche; gizmo", "Selezione e oggetto attivo", "Muovere, ruotare, scalare (`G`, `R`, `S`) con assi e valori numerici", "`N` → Item: Location, Rotation, Scale precise", "Aggiungere, eliminare, duplicare", "Salvare e annullare; salvataggio versionato"],
   "prove": [("B autonoma", "L01_autonoma_v02.blend", "5/5", "Superata", "10/10"), ("C rotazioni", "L01_autonoma_v03.blend", "5/5", "Superata", "10/10")],
   "osserv": ["Posizioni, scale e rotazioni esatte, versionamento corretto (v01–v03).", "Nessun punto perso."],
   "ripasso": ["Nessuno."]},
  "L02": {"titolo": "Edit Mode e modellazione base", "cartella": "L02_edit_mode_e_modellazione_base", "data": "2026-10-13", "stato": "Completata", "voto": "9/10",
   "argomenti": ["Edit Mode: vertici, spigoli, facce; selezione", "Statistics: leggere i numeri della mesh", "Extrude, Inset, Loop Cut, Bevel con valori numerici", "Apply Scale prima di Inset/Bevel/modificatori", "Normali e mesh chiusa (manifold)", "Riparare buchi, vertici sciolti, normali"],
   "prove": [("A guidata (Sgabello)", "L02_guidata_v02.blend", "controlli superati", "Superata", "10/10"), ("B autonoma (Tavolino)", "L02_autonoma_v02.blend", "controlli superati", "Superata", "10/10"), ("C riparazione", "L02_riparata_v01.blend", "6/6", "Superata", "10/10"), ("Bevel", "consegne_L02_bevel_v02.blend", "10/10", "Superata", "10/10"), ("C diagnosi scritta", "risposte scritte", "—", "Da consolidare", "7/10")],
   "osserv": ["Quattro file perfetti.", "Punto perso solo nella diagnosi scritta: risposte 2, 4 e 6 imprecise (termini generici, causa principale non indicata)."],
   "ripasso": ["Descrivere i difetti di una mesh con termini verificabili (mesh non chiusa, normali invertite, facce interne…)."]},
  "L03": {"titolo": "Collezioni, gerarchie, unità, presentazione", "cartella": "L03_collezioni_gerarchie_unita_presentazione", "data": "2026-10-14", "stato": "Completata", "voto": "9/10",
   "argomenti": ["Outliner e collezioni", "Gerarchie (parent), Keep Transform, Empty come root", "Nomi esatti e origine degli oggetti", "Unità in millimetri (Unit Scale 0,001)", "Immagine di riferimento", "Salvataggio sicuro e backup", "Render semplice in Eevee e PNG", "Riparare normali invertite, facce interne, vertici doppi (`M` → By Distance)"],
   "prove": [("A guidata (casetta)", "L03_guidata_v02.blend", "17/18 (refuso nel nome)", "Superata", "9/10"), ("B autonoma", "L03_autonoma_v02.blend", "22/22", "Superata", "10/10"), ("C riparazione", "L03_diagnosi_riparata_v03.blend", "3/3", "Superata", "10/10"), ("Render", "L03_casetta_render_v01.png", "1600×900, ombre", "Superata", "9/10")],
   "osserv": ["Punti persi: refuso `Caa_Tetto` nel nome e frase causale finale assente.", "Chiude il Blocco 1 (Fondamenti)."],
   "ripasso": ["Nomi esatti degli oggetti.", "Frase causale: «Poiché…, …, quindi…»."]},
  "L04": {"titolo": "Modificatori: Mirror, Solidify, Array", "cartella": "L04_modificatori_mirror_array_solidify", "data": "2026-10-14", "stato": "Completata", "voto": "8/10",
   "argomenti": ["Modificatori non distruttivi e stack", "Mirror: metà modello, origine sul piano, Merge Vertices", "Solidify: spessore, Offset, Even Thickness, Scale 1", "Array: Count e Offset relativo (L+G)/L", "Ordine dei modificatori: Mirror → Solidify → Array", "Controllare il risultato su una copia con Apply"],
   "prove": [("A guidata (vaschette)", "L04_guidata_v02.blend", "13/13", "Superata", "10/10"), ("B autonoma (cornice)", "L04_autonoma_v05.blend", "13/13 alla v05 (v02 11/13, v03 8/13, v04 12/13)", "Superata alla 5ª versione", "8/10"), ("C stack sbagliati", "L04_stack_riparato_v02.blend", "3/3", "Superata", "10/10"), ("Frasi causali", "risposte scritte", "—", "Da consolidare", "—")],
   "osserv": ["Parte B superata dopo tre revisioni: nome dell'oggetto, scala usata per forzare le dimensioni (Scale ≠ 1), quota Z.", "Frasi causali ancora con errori di contenuto (Vaschetta_3: il Merge «raddoppia» i corpi, al contrario).", "Soluzione originale della cornice con pareti verticali + Solidify (volume esatto)."],
   "ripasso": ["Correggere la causa (geometria) e non il sintomo (scala).", "Frasi causali senza errori di contenuto."]},
  "L05": {"titolo": "Subdivision Surface e controllo degli spigoli", "cartella": "L05_subdivision_surface_e_spigoli", "data": "avvio 2026-10-15", "stato": "In corso (Parte B da ripetere)", "voto": "da assegnare",
   "argomenti": ["Subdivision Surface: livelli Viewport e Render", "Perché un cubo si restringe (33,58 mm, volume 31%)", "Anelli di supporto con Inset Individual", "Crease (`Shift`+`E`) e confronto con i supporti", "Shade Smooth e Flat", "Base solo quad", "Misurare il risultato su una copia con Apply"],
   "prove": [("A guidata (blocchi)", "L05_guidata_v02.blend", "11/12 (nome `Blocco_Crease`)", "Superata", "9/10"), ("B autonoma (sapone)", "L05_autonoma_v03.blend", "v02 12/16, v03 11/16; v04 in attesa", "Non superata", "—"), ("C riparazione", "L05_blocchi_riparati_v02.blend", "3/3", "Superata", "10/10"), ("C diagnosi scritta", "Risposte.txt", "—", "Da consolidare", "7/10")],
   "osserv": ["Guidata: l'unico punto perso è il nome (`Blocco_Crease` invece di `Blocco_crease`): quarto caso sui nomi.", "Diagnosi: struttura corretta; Blocco_3 con conseguenza falsa (Flat/Smooth non cambia la stampa); mancano meccanismo e numeri.", "Parte B: v03 con Subdivision applicato, Flat Shading, lati corti arrotondati su circa 20 mm. Traccia passo-passo fornita (05_traccia_parte_B.pdf): se superata con la traccia, sarà registrata come «superata con traccia»."],
   "ripasso": ["Controllare tutto il perimetro dei supporti (12 spigoli).", "Non applicare il modificatore.", "Nomi esatti (maiuscole)."]},
 },
}

def media(voti):
    n = [float(v.split("/")[0]) for v in voti]; return sum(n) / len(n)

def scheda(codice, d, blocco):
    r = [f"# Scheda registro {codice} — {d['titolo']}", "",
         f"**Blocco {blocco['n']}: {blocco['nome']}** · **Data:** {d['data']} · **Stato:** {d['stato']}", "",
         f"## Voto finale: {d['voto']}", "",
         "## Argomenti trattati (spunta quando li sai spiegare a parole tue)", "", "| ☐ | Argomento |", "|---|---|"]
    r += [f"| ☐ | {a} |" for a in d["argomenti"]]
    r += ["", "## Prove ed esiti (compilati dal tutor nel registro online)", "", "| Parte | File | Controlli | Esito | Voto |", "|---|---|---|---|---|"]
    r += [f"| {p[0]} | `{p[1]}` | {p[2]} | {p[3]} | {p[4]} |" for p in d["prove"]]
    r += ["", "## Osservazioni del tutor", ""] + [f"- {o}" for o in d["osserv"]]
    r += ["", "## Da ripassare", ""] + [f"- ☐ {x}" for x in d["ripasso"]]
    r += ["", "## Le mie note", "", "<div style=\"border:1px solid #888; height:45mm\"></div>", "",
          "**Trascritto sul mio quaderno il** ____________  **Firma** ____________",
          "", f"*Scheda generata dal registro online il {AGGIORNATO}. Se lo stato cambia, scrivimi e rigenero.*"]
    return "\n".join(r) + "\n"

def registro():
    r = ["# Registro delle attività — 3D ART MASTER ACADEMY", "",
         f"**Allievo:** ______________________  **Ultimo aggiornamento:** {AGGIORNATO}", "",
         "Contiene **solo le lezioni già preparate o svolte**. Nuove lezioni e nuovi blocchi si aggiungono man mano che sono certi. Il voto di ogni lezione ha sempre un motivo verificabile (vedi la scheda della lezione).", "",
         "Ogni lezione ha una scheda stampabile `LEZIONI/<cartella>/scheda_registro_LXX.pdf` con argomenti, esiti e voti: la compili tu a mano ricopiando il registro online.", ""]
    for b in DATI["blocchi"]:
        voti = [DATI["lezioni"][c]["voto"] for c in b["lezioni"] if "/" in DATI["lezioni"][c]["voto"]]
        completo = all("/" in DATI["lezioni"][c]["voto"] for c in b["lezioni"])
        r += [f"## Blocco {b['n']} — {b['nome']}", "", f"**Prova del blocco:** {b['prova']}", "",
              "| Lezione | Data | Argomento | Stato | Voto finale |", "|---|---|---|---|---|"]
        for c in b["lezioni"]:
            d = DATI["lezioni"][c]; r.append(f"| {c} | {d['data']} | {d['titolo']} | {d['stato']} | **{d['voto']}** |")
        if completo:
            r += ["", f"**Media delle lezioni del blocco:** {media(voti):.1f}/10 (media aritmetica semplice)."]
        else:
            r += ["", f"**Media parziale ({len(voti)} {'lezione' if len(voti) == 1 else 'lezioni'} con voto):** {media(voti):.1f}/10. Il blocco non è ancora chiuso."]
        r.append("")
    r += ["## Dettaglio per lezione", ""]
    for b in DATI["blocchi"]:
        for c in b["lezioni"]:
            d = DATI["lezioni"][c]
            r += [f"### {c} — {d['titolo']} · {d['voto']}", "", "| Parte | File | Controlli | Esito | Voto |", "|---|---|---|---|---|"]
            r += [f"| {p[0]} | `{p[1]}` | {p[2]} | {p[3]} | {p[4]} |" for p in d["prove"]]
            r += [""] + [f"- {o}" for o in d["osserv"]] + [""]
    r += ["## Riepilogo voti", "", "| Lezione | " + " | ".join(DATI["lezioni"]) + " |", "|---|" + "---|" * len(DATI["lezioni"]),
          "| Voto | " + " | ".join(DATI["lezioni"][c]["voto"].replace("/10", "") for c in DATI["lezioni"]) + " |"]
    return "\n".join(r) + "\n"

if __name__ == "__main__":
    for b in DATI["blocchi"]:
        for c in b["lezioni"]:
            d = DATI["lezioni"][c]
            path = os.path.join(ROOT, "LEZIONI", d["cartella"], f"scheda_registro_{c}.md")
            open(path, "w").write(scheda(c, d, b)); print("OK", os.path.relpath(path, ROOT))
    open(os.path.join(ROOT, "REGISTRO.md"), "w").write(registro()); print("OK REGISTRO.md")
