"""Verifica la Parte C della Lezione 5 (riparazione dei tre blocchi di L05_blocchi_sbagliati.blend). NON modifica il file.
Uso:  blender -b --factory-startup <file.blend> --python verifica_L05_C.py
"""
import bpy, bmesh
from mathutils import Vector
res = []
def chk(ok, a, b): res.append((bool(ok), a if ok else b))
for nome in ("Blocco_1", "Blocco_2", "Blocco_3"):
    o = bpy.data.objects.get(nome)
    if o is None or o.type != 'MESH': chk(False, "", f"{nome} non trovato"); continue
    dg = bpy.context.evaluated_depsgraph_get(); oe = o.evaluated_get(dg); me = oe.to_mesh()
    bm = bmesh.new(); bm.from_mesh(me); bm.transform(o.matrix_world); bm.normal_update(); oe.to_mesh_clear()
    mn = Vector([min(v.co[i] for v in bm.verts) for i in range(3)]); mx = Vector([max(v.co[i] for v in bm.verts) for i in range(3)]); d = mx - mn
    nm = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    vol = sum(f.calc_area() * (f.calc_center_median().dot(f.normal)) / 3.0 for f in bm.faces)
    bm.free()
    subs = [m for m in o.modifiers if m.type == 'SUBSURF']
    stack_ok = len(o.modifiers) == 1 and len(subs) == 1 and subs[0].levels == 2 and subs[0].show_viewport and len(o.data.vertices) < 300
    smooth = all(p.use_smooth for p in o.data.polygons)
    nq = sum(1 for p in o.data.polygons if len(p.vertices) != 4)
    pos_ok = abs(o.location.z - 20) < 1e-3 and abs(o.location.y) < 1e-3 and abs(o.location.x - {"Blocco_1": -70, "Blocco_2": 0, "Blocco_3": 70}[nome]) < 1e-3
    sc_ok = all(abs(s - 1) < 1e-4 for s in o.scale)
    ok = (stack_ok and smooth and nq == 0 and pos_ok and sc_ok and nm == 0 and all(abs(d[i] - 40) <= 0.4 for i in range(3)) and 55000 <= vol <= 60200)
    chk(ok, f"{nome}: Subdivision livello 2 non applicato, Smooth, quad, 40×40×40 mm, spigoli arrotondati (volume {vol:.0f} mm³), chiuso",
        f"{nome}: dimensioni {d.x:.1f}×{d.y:.1f}×{d.z:.1f} (attese 40), volume {vol:.0f} mm³ (finestra 55000–60200), Smooth {smooth}, "
        f"stack {[m.type for m in o.modifiers]} livello {subs[0].levels if subs else None}, vertici base {len(o.data.vertices)}, non-quad {nq}, "
        f"scala {tuple(round(s,2) for s in o.scale)}, posizione {tuple(round(v,1) for v in o.location)}, non-manifold {nm}")
print("\n=== VERIFICA L05 Parte C ===")
for ok, t in res: print(("[OK]     " if ok else "[ERRORE] ") + t)
n = sum(1 for ok, _ in res if ok); print(f"RISULTATO: {n}/{len(res)} controlli -> {'SUPERATA' if n == len(res) else 'NON SUPERATA'}")
