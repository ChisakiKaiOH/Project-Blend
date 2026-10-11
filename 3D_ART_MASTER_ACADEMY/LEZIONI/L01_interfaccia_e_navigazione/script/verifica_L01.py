"""Verifica la consegna della Lezione 1 (Blender 5.0.1). NON modifica il file.
Uso:  blender -b --factory-startup <file.blend> --python verifica_L01.py -- <A|B|C>
  A = parte guidata, B = prova autonoma (default B), C = verifica delle rotazioni
Confronta la geometria reale nello spazio mondo (non gli angoli Euler): rotazioni diverse
che producono lo stesso risultato sono accettate. Valori attesi: SCRIPT_BLENDER/L01_target_<A|B|C>.json
"""
import bpy, sys, os, json
from mathutils import Vector

var = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "B"
TARGET = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"L01_target_{var}.json")))
TOL_C, TOL_B = 0.15, 0.2

def misure(o):
    vs = [o.matrix_world @ v.co for v in o.data.vertices]
    c = sum(vs, Vector()) / len(vs)
    return c, [min(v[i] for v in vs) for i in range(3)], [max(v[i] for v in vs) for i in range(3)]

ok_tot, righe = 0, []
presenti = {o.name: o for o in bpy.data.objects if o.type == 'MESH'}
for nome, t in TARGET.items():
    o = presenti.get(nome)
    if o is None:
        righe.append(f"[MANCA]  {nome}: oggetto non trovato (controlla il nome, maiuscole comprese)"); continue
    c, mn, mx = misure(o); err = []
    for i, ax in enumerate("XYZ"):
        if abs(c[i] - t["centro"][i]) > TOL_C: err.append(f"centro {ax}={c[i]:.2f} (atteso {t['centro'][i]:.2f})")
        if abs(mn[i] - t["min"][i]) > TOL_B or abs(mx[i] - t["max"][i]) > TOL_B:
            err.append(f"ingombro {ax}=[{mn[i]:.2f},{mx[i]:.2f}] (atteso [{t['min'][i]:.2f},{t['max'][i]:.2f}])")
    if err: righe.append(f"[ERRORE] {nome}: " + "; ".join(err))
    else: ok_tot += 1; righe.append(f"[OK]     {nome}")
for n in sorted(x for x in presenti if x not in TARGET and x != "Pavimento"):
    righe.append(f"[EXTRA]  {n}: oggetto non previsto (non penalizza, ma verifica che sia voluto)")
print(f"\n=== VERIFICA L01 (disposizione {var}) ==="); print("\n".join(righe))
print(f"RISULTATO: {ok_tot}/{len(TARGET)} oggetti corretti -> {'SUPERATA' if ok_tot == len(TARGET) else 'NON SUPERATA'}")
