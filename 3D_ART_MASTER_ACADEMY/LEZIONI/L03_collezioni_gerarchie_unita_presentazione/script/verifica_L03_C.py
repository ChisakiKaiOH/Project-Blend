"""Verifica la Parte C della Lezione 3 (riparazione dei tre oggetti di L03_mesh_diagnosi.blend). NON modifica il file.
Uso:  blender -b --factory-startup <file.blend> --python verifica_L03_C.py
"""
import bpy, bmesh
res = []
def chk(ok, a, b): res.append((bool(ok), a if ok else b))
for nome in ("Oggetto_A", "Oggetto_B", "Oggetto_C"):
    o = bpy.data.objects.get(nome)
    if o is None or o.type != 'MESH': chk(False, "", f"{nome} non trovato"); continue
    bm = bmesh.new(); bm.from_mesh(o.data); bm.transform(o.matrix_world); bm.normal_update()
    nm = sum(1 for e in bm.edges if len(e.link_faces) != 2); loose = sum(1 for v in bm.verts if not v.link_edges)
    vol = sum(f.calc_area() * (f.calc_center_median().dot(f.normal)) / 3.0 for f in bm.faces)
    dbl = len(bmesh.ops.find_doubles(bm, verts=bm.verts, dist=1e-4)["targetmap"])
    seen, shells = set(), 0
    for v in bm.verts:
        if v.index in seen: continue
        shells += 1; st = [v]; seen.add(v.index)
        while st:
            c = st.pop()
            for e in c.link_edges:
                w = e.other_vert(c)
                if w.index not in seen: seen.add(w.index); st.append(w)
    ok = nm == 0 and loose == 0 and shells == 1 and dbl == 0 and abs(vol - 8000) < 160 and not o.modifiers
    chk(ok, f"{nome}: chiuso, 1 corpo, normali verso l'esterno, nessun vertice doppio (volume {vol:.0f} mm³)",
        f"{nome}: {nm} spigoli non-manifold, {loose} vertici sciolti, {shells} corpi, {dbl} vertici doppi, volume {vol:.0f} mm³ (atteso ≈ 8000), modificatori: {len(o.modifiers)}")
    bm.free()
print("\n=== VERIFICA L03 Parte C ===")
for ok, t in res: print(("[OK]     " if ok else "[ERRORE] ") + t)
n = sum(1 for ok, _ in res if ok); print(f"RISULTATO: {n}/{len(res)} controlli -> {'SUPERATA' if n == len(res) else 'NON SUPERATA'}")
