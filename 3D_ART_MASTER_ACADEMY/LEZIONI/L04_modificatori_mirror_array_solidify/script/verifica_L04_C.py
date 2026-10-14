"""Verifica la Parte C della Lezione 4 (riparazione delle tre vaschette di L04_stack_sbagliato.blend). NON modifica il file.
Uso:  blender -b --factory-startup <file.blend> --python verifica_L04_C.py
"""
import bpy, bmesh
from mathutils import Vector
res = []
def chk(ok, a, b): res.append((bool(ok), a if ok else b))
for nome in ("Vaschetta_1", "Vaschetta_2", "Vaschetta_3"):
    o = bpy.data.objects.get(nome)
    if o is None or o.type != 'MESH': chk(False, "", f"{nome} non trovato"); continue
    ordine = [m.type for m in o.modifiers]
    dg = bpy.context.evaluated_depsgraph_get(); oe = o.evaluated_get(dg); me = oe.to_mesh()
    bm = bmesh.new(); bm.from_mesh(me); bm.transform(o.matrix_world); bm.normal_update(); oe.to_mesh_clear()
    mn = Vector([min(v.co[i] for v in bm.verts) for i in range(3)]); mx = Vector([max(v.co[i] for v in bm.verts) for i in range(3)]); d = mx - mn
    nm = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    vol = sum(f.calc_area() * (f.calc_center_median().dot(f.normal)) / 3.0 for f in bm.faces)
    dbl = len(bmesh.ops.find_doubles(bm, verts=bm.verts, dist=1e-3)["targetmap"])
    seen, sh = set(), 0
    for v in bm.verts:
        if v.index in seen: continue
        sh += 1; st = [v]; seen.add(v.index)
        while st:
            c = st.pop()
            for e in c.link_edges:
                w = e.other_vert(c)
                if w.index not in seen: seen.add(w.index); st.append(w)
    mir = next((m for m in o.modifiers if m.type == 'MIRROR'), None)
    sc_ok = all(abs(s - 1) < 1e-4 for s in o.scale)
    ok = (ordine == ['MIRROR', 'SOLIDIFY'] and mir is not None and mir.use_mirror_merge and sc_ok and nm == 0 and sh == 1 and dbl == 0
          and abs(d.x - 80) <= 0.3 and abs(d.y - 50) <= 0.3 and abs(d.z - 20) <= 0.3 and abs(vol - 17072) <= 17072 * 0.015)
    chk(ok, f"{nome}: stack Mirror → Solidify, scala 1, chiusa, 1 corpo, volume {vol:.0f} mm³",
        f"{nome}: stack {'→'.join(ordine)}, scala {tuple(round(s,2) for s in o.scale)}, Merge {mir.use_mirror_merge if mir else None}, "
        f"{nm} spigoli non-manifold, {sh} corpi, {dbl} vertici doppi, volume {vol:.0f} mm³ (atteso 17072), dimensioni {d.x:.0f}×{d.y:.0f}×{d.z:.0f}")
    bm.free()
print("\n=== VERIFICA L04 Parte C ===")
for ok, t in res: print(("[OK]     " if ok else "[ERRORE] ") + t)
n = sum(1 for ok, _ in res if ok); print(f"RISULTATO: {n}/{len(res)} controlli -> {'SUPERATA' if n == len(res) else 'NON SUPERATA'}")
