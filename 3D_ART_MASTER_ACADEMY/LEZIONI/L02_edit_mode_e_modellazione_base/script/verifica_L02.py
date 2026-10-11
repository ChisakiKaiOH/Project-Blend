"""Verifica la consegna della Lezione 2 (Blender 5.0.1). NON modifica il file.
Uso:  blender -b --factory-startup <file.blend> --python verifica_L02.py -- <A|B>
  A = Sgabello (parte guidata), B = Tavolino (prova autonoma)
Controlli: nome, modificatori, scala applicata, dimensioni, base a Z=0, mesh chiusa (manifold),
normali verso l'esterno, un solo corpo, nessun vertice doppio, 4 gambe a filo degli angoli, spessore del piano.
"""
import bpy, bmesh, sys
from mathutils import Vector

var = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "B"
SPEC = {"A": dict(nome="Sgabello", dim=(0.30, 0.30, 0.45), gamba=(0.10, 0.02), piano=(0.03, 0.005)),
        "B": dict(nome="Tavolino", dim=(0.60, 0.40, 0.45), gamba=(0.04, 0.015), piano=(0.03, 0.01))}[var]
TOL_DIM = 0.01
res = []   # (esito, descrizione)
def chk(ok, ok_txt, ko_txt): res.append((bool(ok), ok_txt if ok else ko_txt))

o = bpy.data.objects.get(SPEC["nome"])
if o is None or o.type != 'MESH':
    print(f"\n=== VERIFICA L02 ({SPEC['nome']}) ===\n[ERRORE] Oggetto '{SPEC['nome']}' non trovato (nome esatto, maiuscole comprese)\nRISULTATO: 0/10 -> NON SUPERATA"); sys.exit(0)

chk(not o.modifiers, "Nessun modificatore", f"Ci sono {len(o.modifiers)} modificatori: questa lezione chiede una mesh senza modificatori")
sc_ok = all(abs(s - 1) < 1e-4 for s in o.scale) and all(abs(r) < 1e-4 for r in o.rotation_euler)
chk(sc_ok, "Scala = 1 e rotazione = 0 (Apply fatto)", f"Scala={tuple(round(s,3) for s in o.scale)} rot={tuple(round(r,3) for r in o.rotation_euler)}: applica con Ctrl+A")

bm = bmesh.new(); bm.from_mesh(o.data); bm.transform(o.matrix_world); bm.normal_update()
bm.verts.ensure_lookup_table(); bm.edges.ensure_lookup_table(); bm.faces.ensure_lookup_table()
mn = Vector([min(v.co[i] for v in bm.verts) for i in range(3)]); mx = Vector([max(v.co[i] for v in bm.verts) for i in range(3)])
dim = mx - mn
chk(all(abs(dim[i] - SPEC["dim"][i]) <= TOL_DIM for i in range(3)),
    f"Dimensioni {dim.x:.3f} x {dim.y:.3f} x {dim.z:.3f} m",
    f"Dimensioni {dim.x:.3f} x {dim.y:.3f} x {dim.z:.3f} m (attese {SPEC['dim'][0]} x {SPEC['dim'][1]} x {SPEC['dim'][2]}, tolleranza 1 cm)")
chk(abs(mn.z) <= TOL_DIM, "Base appoggiata al pavimento (Z min = 0)", f"Z minima = {mn.z:.3f} m (attesa 0)")

nm = [e for e in bm.edges if len(e.link_faces) != 2]
loose = [v for v in bm.verts if not v.link_edges]
chk(not nm and not loose, "Mesh chiusa: nessuno spigolo non-manifold, nessun vertice sciolto",
    f"Mesh NON chiusa: {len(nm)} spigoli non-manifold, {len(loose)} vertici sciolti (Select → Select All by Trait)")
# componenti connesse
seen, shells = set(), 0
for v in bm.verts:
    if v.index in seen: continue
    shells += 1; st = [v]; seen.add(v.index)
    while st:
        c = st.pop()
        for e in c.link_edges:
            w = e.other_vert(c)
            if w.index not in seen: seen.add(w.index); st.append(w)
chk(shells == 1, "Un solo corpo (gambe unite al piano)", f"{shells} corpi separati: gambe non unite al piano, oppure geometria isolata (vertici o spigoli sciolti)")
vol = sum(f.calc_area() * (f.calc_center_median().dot(f.normal)) / 3.0 for f in bm.faces)
chk(vol > 0, f"Normali verso l'esterno (volume {vol:.5f} m³)", f"Normali invertite o mesh aperta (volume calcolato {vol:.5f}): usa Mesh → Normals → Recalculate Outside")
import bmesh as _b
dbl = _b.ops.find_doubles(bm, verts=bm.verts, dist=1e-4)["targetmap"]
chk(not dbl, "Nessun vertice doppio", f"{len(dbl)} vertici sovrapposti (Mesh → Merge → By Distance)")

# gambe: facce rivolte in basso alla quota minima
zl = mn.z + 0.005
basse = [f for f in bm.faces if f.normal.z < -0.99 and f.calc_center_median().z <= zl]
ok_g = len(basse) == 4; info = f"{len(basse)} facce di appoggio"
if ok_g:
    w_tgt, w_tol = SPEC["gamba"]; quad = set()
    for f in basse:
        xs = [v.co.x for v in f.verts]; ys = [v.co.y for v in f.verts]
        wx, wy = max(xs) - min(xs), max(ys) - min(ys)
        flush = (abs(min(xs) - mn.x) < 0.01 or abs(max(xs) - mx.x) < 0.01) and (abs(min(ys) - mn.y) < 0.01 or abs(max(ys) - mx.y) < 0.01)
        if abs(wx - w_tgt) > w_tol or abs(wy - w_tgt) > w_tol or not flush: ok_g = False; info = f"gamba {wx:.3f}x{wy:.3f} m, a filo con l'angolo: {flush}"
        quad.add((f.calc_center_median().x > (mn.x + mx.x) / 2, f.calc_center_median().y > (mn.y + mx.y) / 2))
    if len(quad) != 4: ok_g = False; info = "le 4 gambe non sono una per angolo"
chk(ok_g, f"4 gambe a filo degli angoli, sezione ≈ {SPEC['gamba'][0]} m", f"Gambe non corrette: {info} (attese 4, sezione {SPEC['gamba'][0]}±{SPEC['gamba'][1]} m, una per angolo)")

# spessore del piano: facce rivolte in basso sopra la quota delle gambe
sotto = [f for f in bm.faces if f.normal.z < -0.99 and f.calc_center_median().z > mn.z + 0.05]
if sotto:
    zs = sum(f.calc_center_median().z for f in sotto) / len(sotto); sp = mx.z - zs
    chk(abs(sp - SPEC["piano"][0]) <= SPEC["piano"][1], f"Spessore del piano {sp:.3f} m", f"Spessore del piano {sp:.3f} m (atteso {SPEC['piano'][0]}±{SPEC['piano'][1]})")
else: chk(False, "", "Non trovo la faccia inferiore del piano")

tri = sum(1 for f in bm.faces if len(f.verts) == 3); ng = sum(1 for f in bm.faces if len(f.verts) > 4)
print(f"\n=== VERIFICA L02 ({SPEC['nome']}) ===")
for ok, t in res: print(("[OK]     " if ok else "[ERRORE] ") + t)
print(f"[INFO]   {len(bm.verts)} vertici, {len(bm.edges)} spigoli, {len(bm.faces)} facce ({tri} triangoli, {ng} n-gon)")
n_ok = sum(1 for ok, _ in res if ok)
print(f"RISULTATO: {n_ok}/{len(res)} controlli -> {'SUPERATA' if n_ok == len(res) else 'NON SUPERATA'}")
