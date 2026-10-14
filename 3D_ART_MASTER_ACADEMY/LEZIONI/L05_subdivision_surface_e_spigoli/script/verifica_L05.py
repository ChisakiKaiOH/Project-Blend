"""Verifica le Parti A e B della Lezione 5. NON modifica il file.
Uso:  blender -b --factory-startup <file.blend> --python verifica_L05.py -- A|B
  A = guidata: oggetti Blocco (supporti) e Blocco_crease (crease)      B = autonoma: Sapone
"""
import bpy, bmesh, sys
from mathutils import Vector
parte = sys.argv[sys.argv.index("--") + 1].upper() if "--" in sys.argv else "B"
res = []
def chk(ok, a, b): res.append((bool(ok), a if ok else b))

def misura(o):
    dg = bpy.context.evaluated_depsgraph_get(); oe = o.evaluated_get(dg); me = oe.to_mesh()
    bm = bmesh.new(); bm.from_mesh(me); bm.transform(o.matrix_world); bm.normal_update(); oe.to_mesh_clear()
    mn = Vector([min(v.co[i] for v in bm.verts) for i in range(3)]); mx = Vector([max(v.co[i] for v in bm.verts) for i in range(3)])
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
    return bm, mn, mx, nm, vol, dbl, sh

def zmax_in(bm, c, x0, x1, y0, y1):
    z = [v.co.z for v in bm.verts if x0 <= abs(v.co.x - c.x) <= x1 and y0 <= abs(v.co.y - c.y) <= y1]
    return max(z) if z else None

def comuni(o, nome, dims, vol_lo, vol_hi, zmin=0.0):
    """Controlli condivisi. Restituisce (bm, mn, mx) o None."""
    coll = [c.name for c in o.users_collection]
    chk(o.name == nome and coll == ["Modello"], f"Oggetto «{nome}» nella collezione Modello",
        f"nome «{o.name}» o collezione {coll} non corretti (atteso «{nome}» in Modello)")
    sc_ok = all(abs(s - 1) < 1e-4 for s in o.scale) and all(abs(r) < 1e-4 for r in o.rotation_euler)
    chk(sc_ok, f"{nome}: Scale 1, rotazione 0", f"{nome}: Scale {tuple(round(s,3) for s in o.scale)}, rotazione {tuple(round(r,3) for r in o.rotation_euler)}")
    subs = [m for m in o.modifiers if m.type == 'SUBSURF']
    ok = len(o.modifiers) == 1 and len(subs) == 1 and subs[0].show_viewport and subs[0].show_render and subs[0].levels == 2 and subs[0].render_levels == 3 \
        and len(o.data.vertices) < 300
    chk(ok, f"{nome}: un solo modificatore Subdivision Surface attivo, Levels Viewport 2, Render 3, non applicato",
        f"{nome}: modificatori {[m.type for m in o.modifiers]}, livelli {(subs[0].levels, subs[0].render_levels) if subs else None}, vertici della base {len(o.data.vertices)} (se sono tanti, l'hai applicato)")
    nq = sum(1 for p in o.data.polygons if len(p.vertices) != 4)
    chk(nq == 0, f"{nome}: la mesh di base ha solo quad", f"{nome}: {nq} facce non quad (triangoli o n-gon) nella mesh di base")
    chk(all(p.use_smooth for p in o.data.polygons), f"{nome}: ombreggiatura Smooth su tutte le facce", f"{nome}: ci sono facce in Flat Shading")
    bm, mn, mx, nm, vol, dbl, sh = misura(o); d = mx - mn
    chk(all(abs(d[i] - dims[i]) <= 0.4 for i in range(3)), f"{nome}: dimensioni finali {dims[0]:g}×{dims[1]:g}×{dims[2]:g} mm (i supporti tengono le facce piatte)",
        f"{nome}: dimensioni finali {d.x:.2f}×{d.y:.2f}×{d.z:.2f} mm (attese {dims[0]:g}×{dims[1]:g}×{dims[2]:g})")
    chk(abs(mn.z - zmin) <= 0.4, f"{nome}: poggia sul piano (Z minima 0)", f"{nome}: Z minima {mn.z:.2f} (attesa 0)")
    chk(vol_lo <= vol <= vol_hi, f"{nome}: spigoli arrotondati nella misura giusta (volume {vol:.0f} mm³)",
        f"{nome}: volume {vol:.0f} mm³, finestra {vol_lo:.0f}–{vol_hi:.0f}: " + ("spigoli troppo morbidi o forma gonfia" if vol < vol_lo else "spigoli ancora troppo vivi"))
    chk(nm == 0 and sh == 1 and dbl == 0, f"{nome}: mesh chiusa, un corpo, nessun vertice doppio",
        f"{nome}: {nm} spigoli non-manifold, {sh} corpi, {dbl} vertici doppi")
    return bm, mn, mx

u = bpy.context.scene.unit_settings
chk(u.system == 'METRIC' and abs(u.scale_length - 0.001) < 1e-9 and u.length_unit == 'MILLIMETERS', "Unità in millimetri", f"Unità: {u.system}, scala {u.scale_length}, {u.length_unit}")
radice = [o.name for o in bpy.context.scene.collection.objects]
chk(not radice, "Nessun oggetto fuori dalle collezioni", f"Oggetti nella radice della scena: {radice}")

if parte == "A":
    o = bpy.data.objects.get("Blocco")
    if o is None or o.type != 'MESH': chk(False, "", "Oggetto «Blocco» non trovato")
    else:
        bm, mn, mx = comuni(o, "Blocco", (40, 40, 40), 55000, 60200); bm.free()
        c = bpy.data.objects.get("Blocco_crease")
        if c is None or c.type != 'MESH': chk(False, "", "Oggetto «Blocco_crease» non trovato")
        else:
            at = c.data.attributes.get("crease_edge")
            vals = [d.value for d in at.data] if at else []
            subs = [m for m in c.modifiers if m.type == 'SUBSURF']
            ok = (len(c.data.vertices) == 8 and at is not None and len(vals) == 12 and all(0.45 <= v <= 0.55 for v in vals)
                  and len(subs) == 1 and subs[0].levels == 2 and all(abs(s - 1) < 1e-4 for s in c.scale) and [x.name for x in c.users_collection] == ["Modello"])
            chk(ok, "Blocco_crease: cubo di 8 vertici, Subdivision livello 2, Crease 0,5 su tutti i 12 spigoli, Scale 1, in Modello",
                f"Blocco_crease: {len(c.data.vertices)} vertici (attesi 8), crease {sorted(set(round(v,2) for v in vals)) if vals else 'assente'}, "
                f"Subdivision {[(m.levels) for m in subs]}, scala {tuple(round(s,3) for s in c.scale)}")
            b2, mn2, mx2, nm2, vol2, dbl2, sh2 = misura(c); d2 = mx2 - mn2
            ok = all(abs(d2[i] - 40) <= 0.4 for i in range(3)) and 55000 <= vol2 <= 60200 and nm2 == 0 and sh2 == 1 and abs(mn2.z) <= 0.4
            chk(ok, f"Blocco_crease: 40×40×40 mm, poggia sul piano, volume {vol2:.0f} mm³, chiuso", f"Blocco_crease: dimensioni {d2.x:.1f}×{d2.y:.1f}×{d2.z:.1f}, Z min {mn2.z:.1f}, volume {vol2:.0f} (finestra 55000–60200), non-manifold {nm2}, corpi {sh2}")
            b2.free()
else:
    o = bpy.data.objects.get("Sapone")
    if o is None or o.type != 'MESH': chk(False, "", "Oggetto «Sapone» non trovato")
    else:
        bm, mn, mx = comuni(o, "Sapone", (80, 50, 20), 68500, 75500)
        bb = [v.co for v in o.data.vertices]
        lo = [min(p[i] for p in bb) for i in range(3)]; hi = [max(p[i] for p in bb) for i in range(3)]
        db = [hi[i] - lo[i] for i in range(3)]
        chk(abs(db[0]-80) <= 0.4 and abs(db[1]-50) <= 0.4 and abs(db[2]-20) <= 0.4, "Sapone: la mesh di base misura 80×50×20 mm",
            f"Sapone: la mesh di base misura {db[0]:.1f}×{db[1]:.1f}×{db[2]:.1f} mm (attesi 80×50×20)")
        cx, cy = (mn.x + mx.x) / 2, (mn.y + mx.y) / 2; c = Vector((cx, cy, 0))
        chk(abs(cx) <= 1 and abs(cy) <= 1, "Sapone: centrato su X e Y", f"Sapone: centro a X={cx:.1f}, Y={cy:.1f} (atteso 0, 0)")
        W = o.matrix_world
        bv = [W @ v.co for v in o.data.vertices]
        manca = [(sx * 25, sy * 10, z) for sx in (-1, 1) for sy in (-1, 1) for z in (18.5, 20.0)
                 if not any((p - Vector((sx * 25 + cx, sy * 10 + cy, z))).length <= 0.4 for p in bv)]
        chk(not manca, "Sapone: nella mesh di base l'incavo ha le pareti a X ±25, Y ±10 (50×20 mm) e il fondo a Z 18,5 (profondità 1,5 mm)",
            f"Sapone: nella mesh di base mancano vertici in {manca[:4]}{'…' if len(manca) > 4 else ''} (X, Y, Z relativi al centro): le pareti dell'incavo non sono a ±25 / ±10 o la profondità non è 1,5 mm")
        fondo = zmax_in(bm, c, 0, 4, 0, 3)
        chk(fondo is not None and 18.1 <= fondo <= 18.9, f"Sapone: il fondo dell'incavo resta a Z = {fondo:.2f} mm" if fondo else "",
            f"Sapone: fondo dell'incavo a Z = {None if fondo is None else round(fondo,2)} (atteso 18,5 ± 0,4): incavo assente o troppo morbido")
        pa, pb = zmax_in(bm, c, 19, 21.5, 0, 3), zmax_in(bm, c, 24.8, 28, 0, 5)
        chk(pa is not None and pb is not None and pa <= 18.8 and pb >= 19.93,
            f"Sapone: spigolo dell'incavo netto (Z {pa:.2f} a 3 mm dentro, {pb:.2f} a 1–3 mm fuori)" if pa and pb else "",
            f"Sapone: spigolo dell'incavo sfumato (Z {None if pa is None else round(pa,2)} a 3 mm dentro, atteso ≤ 18,8; {None if pb is None else round(pb,2)} a 1–3 mm fuori, atteso ≥ 19,93): servono anelli di supporto vicino al bordo dell'incavo")
        bm.free()
print("\n=== VERIFICA L05 Parte " + parte + " ===")
for ok, t in res: print(("[OK]     " if ok else "[ERRORE] ") + t)
n = sum(1 for ok, _ in res if ok); print(f"RISULTATO: {n}/{len(res)} controlli -> {'SUPERATA' if n == len(res) else 'NON SUPERATA'}")
