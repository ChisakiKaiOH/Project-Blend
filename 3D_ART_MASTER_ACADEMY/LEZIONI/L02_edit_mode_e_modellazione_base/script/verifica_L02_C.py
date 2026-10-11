"""Verifica la Parte C della Lezione 2 (riparazione di L02_mesh_difettosa.blend). NON modifica il file.
Uso:  blender -b --factory-startup <file.blend> --python verifica_L02_C.py
Il cubo riparato deve avere 8 vertici, 12 spigoli, 6 facce, essere chiuso, con un solo corpo e normali verso l'esterno.
"""
import bpy, bmesh
o = bpy.data.objects.get("Difettoso")
if o is None or o.type != 'MESH':
    print("\n=== VERIFICA L02 Parte C ===\n[ERRORE] Oggetto 'Difettoso' non trovato\nRISULTATO: 0/6 -> NON SUPERATA"); raise SystemExit
bm = bmesh.new(); bm.from_mesh(o.data); bm.transform(o.matrix_world); bm.normal_update()
res = []
def chk(ok, a, b): res.append((bool(ok), a if ok else b))
loose = [v for v in bm.verts if not v.link_edges]
chk(not loose, "Nessun vertice sciolto", f"{len(loose)} vertici sciolti (Select → Select All by Trait → Loose Geometry)")
nm = [e for e in bm.edges if len(e.link_faces) != 2]
chk(not nm, "Mesh chiusa: nessuno spigolo non-manifold", f"{len(nm)} spigoli non-manifold: manca ancora una faccia?")
chk(len(bm.faces) == 6, "6 facce", f"{len(bm.faces)} facce (un cubo chiuso ne ha 6)")
chk(len(bm.verts) == 8 and len(bm.edges) == 12, "8 vertici e 12 spigoli", f"{len(bm.verts)} vertici e {len(bm.edges)} spigoli (attesi 8 e 12: hai creato vertici in più?)")
vol = sum(f.calc_area() * (f.calc_center_median().dot(f.normal)) / 3.0 for f in bm.faces)
chk(vol > 0.9, f"Normali verso l'esterno (volume {vol:.3f} m³, atteso ≈ 1)", f"Normali invertite o mesh aperta (volume {vol:.3f}, atteso ≈ 1): Mesh → Normals → Recalculate Outside")
chk(not o.modifiers, "Nessun modificatore", "Ci sono modificatori")
print("\n=== VERIFICA L02 Parte C ===")
for ok, t in res: print(("[OK]     " if ok else "[ERRORE] ") + t)
n = sum(1 for ok, _ in res if ok); print(f"RISULTATO: {n}/{len(res)} controlli -> {'SUPERATA' if n == len(res) else 'NON SUPERATA'}")
