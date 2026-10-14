"""Verifica la consegna della Lezione 4 (Blender 5.0.1). NON modifica il file.
Uso:  blender -b --factory-startup <file.blend> --python verifica_L04.py -- <A|B>
  A = Vaschetta (parte guidata), B = Cornice (prova autonoma)
Valuta la mesh DOPO i modificatori (quella che verrebbe stampata): dimensioni, volume, mesh chiusa, corpi, vertici doppi,
ordine dei modificatori, mesh di partenza dimezzata (simmetria), scala applicata, unità in mm.
"""
import bpy, bmesh, sys
from mathutils import Vector

var = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "B"
SPEC = {"A": dict(nome="Vaschetta", dim=(260, 50, 20), vol=51216.0, corpi=3, mezza_x=-40),
        "B": dict(nome="Cornice", dim=(170, 40, 3), vol=8424.0, corpi=3, mezza_x=-25)}[var]
res = []
def chk(ok, a, b): res.append((bool(ok), a if ok else b))
sc = bpy.context.scene; u = sc.unit_settings
chk(u.system == 'METRIC' and abs(u.scale_length - 0.001) < 1e-9 and u.length_unit == 'MILLIMETERS', "Unità in millimetri",
    f"Unità: {u.system}, scala {u.scale_length}, {u.length_unit} (attesi METRIC, 0.001, MILLIMETERS)")
o = bpy.data.objects.get(SPEC["nome"])
if o is None or o.type != 'MESH':
    print(f"\n=== VERIFICA L04 ({SPEC['nome']}) ===\n[ERRORE] Oggetto '{SPEC['nome']}' non trovato (nome esatto)\nRISULTATO: 0/1 -> NON SUPERATA"); sys.exit(0)

chk(any(c.name == "Modello" for c in o.users_collection) and not sc.collection.objects, "Oggetto nella collezione 'Modello', nessun oggetto fuori dalle collezioni",
    "L'oggetto non è nella collezione 'Modello', oppure ci sono oggetti fuori dalle collezioni")
chk(all(abs(s - 1) < 1e-4 for s in o.scale) and all(abs(r) < 1e-4 for r in o.rotation_euler), "Scala = 1 e rotazione = 0",
    f"Scala {tuple(round(s,3) for s in o.scale)}, rotazione {tuple(round(r,3) for r in o.rotation_euler)}: applica con Ctrl+A → Scale prima dei modificatori")

def tipo(m): return "ARRAY" if (m.type == 'ARRAY' or (m.type == 'NODES' and m.node_group and m.node_group.name.startswith("Array"))) else m.type
ordine = [tipo(m) for m in o.modifiers]
chk(ordine == ["MIRROR", "SOLIDIFY", "ARRAY"], "Stack dei modificatori: Mirror → Solidify → Array",
    f"Stack: {' → '.join(ordine) or '(vuoto)'} (atteso MIRROR → SOLIDIFY → ARRAY, nell'ordine: né applicati né in altra sequenza)")
chk(all(m.show_viewport for m in o.modifiers), "Tutti i modificatori sono attivi", "Almeno un modificatore è disattivato nella viewport")

# mesh di partenza = metà (simmetria)
xs = [v.co.x for v in o.data.vertices]
chk(xs and max(xs) <= 0.05 and abs(min(xs) - SPEC["mezza_x"]) <= 0.3, f"Mesh di partenza dimezzata (X da {min(xs):.0f} a {max(xs):.0f}) e Mirror attivo",
    f"La mesh di partenza non è una metà: X da {min(xs):.1f} a {max(xs):.1f} (atteso da {SPEC['mezza_x']} a 0)" if xs else "La mesh è vuota")
mir = next((m for m in o.modifiers if m.type == 'MIRROR'), None)
chk(mir is not None and mir.use_axis[0] and mir.use_mirror_merge, "Mirror: asse X con Merge Vertices attivo", "Mirror assente, senza asse X o con Merge Vertices spento")

# mesh valutata
dg = bpy.context.evaluated_depsgraph_get(); oe = o.evaluated_get(dg); me = oe.to_mesh()
bm = bmesh.new(); bm.from_mesh(me); bm.transform(o.matrix_world); bm.normal_update(); oe.to_mesh_clear()
if not bm.verts: chk(False, "", "La mesh dopo i modificatori è vuota")
else:
    mn = Vector([min(v.co[i] for v in bm.verts) for i in range(3)]); mx = Vector([max(v.co[i] for v in bm.verts) for i in range(3)]); d = mx - mn
    chk(all(abs(d[i] - SPEC["dim"][i]) <= 0.3 for i in range(3)), f"Dimensioni finali {d.x:.1f} × {d.y:.1f} × {d.z:.1f} mm",
        f"Dimensioni finali {d.x:.1f} × {d.y:.1f} × {d.z:.1f} mm (attese {SPEC['dim'][0]} × {SPEC['dim'][1]} × {SPEC['dim'][2]})")
    chk(abs(mn.z) <= 0.2, "Base a Z = 0", f"Z minima = {mn.z:.2f} mm (attesa 0)")
    nm = sum(1 for e in bm.edges if len(e.link_faces) != 2); loose = sum(1 for v in bm.verts if not v.link_edges)
    chk(nm == 0 and loose == 0, "Mesh finale chiusa: nessuno spigolo non-manifold",
        f"Mesh finale NON chiusa: {nm} spigoli non-manifold, {loose} vertici sciolti (controlla ordine dei modificatori e Merge)")
    seen, sh = set(), 0
    for v in bm.verts:
        if v.index in seen: continue
        sh += 1; st = [v]; seen.add(v.index)
        while st:
            c = st.pop()
            for e in c.link_edges:
                w = e.other_vert(c)
                if w.index not in seen: seen.add(w.index); st.append(w)
    chk(sh == SPEC["corpi"], f"{sh} corpi separati, come previsto", f"{sh} corpi separati (attesi {SPEC['corpi']}): Merge dello Mirror o copie dell'Array non corretti")
    dbl = len(bmesh.ops.find_doubles(bm, verts=bm.verts, dist=1e-3)["targetmap"])
    chk(dbl == 0, "Nessun vertice doppio", f"{dbl} vertici doppi nella mesh finale")
    vol = sum(f.calc_area() * (f.calc_center_median().dot(f.normal)) / 3.0 for f in bm.faces)
    chk(abs(vol - SPEC["vol"]) <= SPEC["vol"] * 0.015, f"Volume {vol:.0f} mm³ (atteso {SPEC['vol']:.0f}): spessori corretti",
        f"Volume {vol:.0f} mm³ (atteso {SPEC['vol']:.0f} ± 1,5%): spessore delle pareti o offset sbagliati (hai attivato Even Thickness?)")
print(f"\n=== VERIFICA L04 ({SPEC['nome']}) ===")
for ok, t in res: print(("[OK]     " if ok else "[ERRORE] ") + t)
n = sum(1 for ok, _ in res if ok); print(f"RISULTATO: {n}/{len(res)} controlli -> {'SUPERATA' if n == len(res) else 'NON SUPERATA'}")
