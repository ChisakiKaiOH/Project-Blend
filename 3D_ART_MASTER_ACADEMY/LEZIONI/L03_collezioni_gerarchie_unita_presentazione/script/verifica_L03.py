"""Verifica la consegna della Lezione 3 (Blender 5.0.1). NON modifica il file.
Uso:  blender -b --factory-startup <file.blend> --python verifica_L03.py -- <A|B>
  A = Casetta (parte guidata), B = riordino della scena disordinata (prova autonoma)
In A controlla anche l'immagine L03_casetta_render_v*.png, se è nella stessa cartella del .blend.
"""
import bpy, bmesh, sys, os, re, glob
from mathutils import Vector

var = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "B"
res = []
def chk(ok, a, b): res.append((bool(ok), a if ok else b))
sc = bpy.context.scene
DEFAULT = re.compile(r"^(Cube|Cylinder|Cone|Sphere|Plane|Torus|Empty|Circle|Icosphere)(\.\d+)?$")

def bbox(o):
    pts = [o.matrix_world @ Vector(c) for c in o.bound_box]
    mn = Vector([min(p[i] for p in pts) for i in range(3)]); mx = Vector([max(p[i] for p in pts) for i in range(3)])
    return mn, mx
def near(a, b, tol=0.5): return all(abs(a[i] - b[i]) <= tol for i in range(3))
def chiusa(o):
    bm = bmesh.new(); bm.from_mesh(o.data)
    n = sum(1 for e in bm.edges if len(e.link_faces) != 2); bm.free(); return n == 0
def in_coll(o, nome): return any(c.name == nome for c in o.users_collection)

u = sc.unit_settings
chk(u.system == 'METRIC' and abs(u.scale_length - 0.001) < 1e-9 and u.length_unit == 'MILLIMETERS',
    "Unità: Metric, Unit Scale 0.001, Length Millimeters",
    f"Unità: system={u.system}, Unit Scale={u.scale_length}, Length={u.length_unit} (attesi METRIC, 0.001, MILLIMETERS)")
chk(not sc.collection.objects, "Nessun oggetto fuori dalle collezioni",
    f"{len(sc.collection.objects)} oggetti nella Scene Collection (non in una collezione): " + ", ".join(o.name for o in sc.collection.objects)[:80])

if var == "A":
    O = bpy.data.objects
    nomi = ["Casa_ROOT", "Casa_Corpo", "Casa_Tetto", "Casa_Porta", "Casa_Camino"]
    mancanti = [n for n in nomi if n not in O]
    chk(not mancanti, "Nomi degli oggetti corretti", "Oggetti mancanti o nome diverso: " + ", ".join(mancanti))
    if not mancanti:
        root = O["Casa_ROOT"]; parti = [O[n] for n in nomi[1:]]
        chk(root.type == 'EMPTY' and root.parent is None and all(p.parent == root for p in parti),
            "Gerarchia: le 4 parti sono figlie di Casa_ROOT (Empty)", "Gerarchia errata: Casa_ROOT deve essere un Empty senza genitore, genitore di tutte e 4 le parti")
        chk(near(root.matrix_world.translation, (0, 0, 0)), "Casa_ROOT a (0, 0, 0)", f"Casa_ROOT in {tuple(round(x,2) for x in root.matrix_world.translation)} (atteso 0,0,0)")
        coll = bpy.data.collections.get("Casa")
        chk(coll and all(in_coll(o, "Casa") for o in [root, *parti]), "Collezione 'Casa' con root e 4 parti", "La collezione 'Casa' manca o non contiene root e 4 parti")
        scn = bpy.data.collections.get("Scena")
        tipi = {o.type for o in scn.objects} if scn else set()
        chk(scn and {'CAMERA', 'LIGHT', 'MESH'} <= tipi, "Collezione 'Scena' con camera, luce e pavimento", "La collezione 'Scena' manca o non contiene camera, luce e pavimento")
        rif = bpy.data.collections.get("Riferimenti")
        ok_rif = rif and any(o.type == 'EMPTY' and o.empty_display_type == 'IMAGE' and o.data for o in rif.objects)
        chk(ok_rif, "Collezione 'Riferimenti' con un'immagine di riferimento", "La collezione 'Riferimenti' manca o non contiene un'immagine (Add → Image → Reference)")
        corpo, tetto, porta, camino = parti
        def dim_ok(o, d, zmin=None):
            mn, mx = bbox(o); dm = mx - mn
            return near(dm, d) and (zmin is None or abs(mn.z - zmin) <= 0.5), dm, mn
        ok, dm, mn = dim_ok(corpo, (60, 40, 40), 0)
        chk(ok, "Corpo 60 × 40 × 40 mm, appoggiato a Z = 0", f"Corpo {dm.x:.1f}×{dm.y:.1f}×{dm.z:.1f} mm, Z min {mn.z:.1f} (atteso 60×40×40, Z min 0)")
        ok, dm, mn = dim_ok(tetto, (66, 46, 20), 40)
        mxz = bbox(tetto)[1].z
        chk(ok and abs(mxz - 60) <= 0.5, "Tetto 66 × 46 × 20 mm, da Z 40 a Z 60", f"Tetto {dm.x:.1f}×{dm.y:.1f}×{dm.z:.1f} mm, Z da {mn.z:.1f} a {mxz:.1f} (atteso 66×46×20, da 40 a 60)")
        vt = [tetto.matrix_world @ v.co for v in tetto.data.vertices]
        colmo = [v for v in vt if v.z > 59.5]
        chk(len(colmo) == 2 and all(abs(v.y) < 0.5 for v in colmo), "Tetto a capanna: colmo di 2 vertici lungo X al centro", f"Il tetto non ha un colmo corretto: {len(colmo)} vertici a Z 60 (attesi 2, al centro, lungo X)")
        ok, dm, mn = dim_ok(porta, (12, 2, 22)); c = (bbox(porta)[0] + bbox(porta)[1]) / 2
        chk(ok and near(c, (0, -20, 11)), "Porta 12 × 2 × 22 mm in (0, -20, 11)", f"Porta {dm.x:.1f}×{dm.y:.1f}×{dm.z:.1f} mm, centro {tuple(round(x,1) for x in c)} (atteso 12×2×22 in 0,-20,11)")
        ok, dm, mn = dim_ok(camino, (8, 8, 20)); c = (bbox(camino)[0] + bbox(camino)[1]) / 2
        chk(ok and near(c, (-20, 10, 58)), "Camino 8 × 8 × 20 mm in (-20, 10, 58)", f"Camino {dm.x:.1f}×{dm.y:.1f}×{dm.z:.1f} mm, centro {tuple(round(x,1) for x in c)} (atteso 8×8×20 in -20,10,58)")
        chk(all(near(p.scale, (1, 1, 1), 1e-3) for p in parti), "Scala applicata (Scale = 1) su tutte le parti", "Almeno una parte ha Scale ≠ 1: applica con Ctrl+A → Scale")
        chk(all(chiusa(p) for p in parti), "Le 4 parti sono mesh chiuse", "Almeno una parte non è chiusa (spigoli non-manifold)")
    r = sc.render
    chk(r.engine == 'BLENDER_EEVEE' and r.resolution_x >= 1280 and r.resolution_percentage == 100, f"Render: EEVEE, {r.resolution_x}×{r.resolution_y}, 100%",
        f"Render: motore {r.engine}, {r.resolution_x}×{r.resolution_y} al {r.resolution_percentage}% (attesi EEVEE, almeno 1280 di larghezza, 100%)")
    chk(sc.camera is not None and sc.camera.type == 'CAMERA', "Camera attiva impostata", "Nessuna camera attiva nella scena")
    cartella = os.path.dirname(bpy.data.filepath); png = sorted(glob.glob(os.path.join(cartella, "L03_casetta_render_v*.png")))
    if not png: chk(False, "", "Immagine di render non trovata: salva il render come L03_casetta_render_v01.png nella stessa cartella del .blend")
    else:
        img = bpy.data.images.load(png[-1]); w, h = img.size; px = img.pixels[:][::3988]
        media = sum(px) / len(px); var_ = sum((p - media) ** 2 for p in px) / len(px)
        chk(w >= 1280 and var_ > 1e-3, f"Immagine {os.path.basename(png[-1])}: {w}×{h}, non uniforme", f"Immagine {os.path.basename(png[-1])}: {w}×{h} (attesa larghezza ≥ 1280) o quasi tutta uniforme")
else:
    CL = {"Albero": ((-40, 30), [(-40, 30, 10), (-40, 30, 35)]),
          "Lampione": ((40, 25), [(40, 25, 2), (40, 25, 24), (40, 25, 48)]),
          "Panchina": ((0, -30), [(0, -30, 20), (-12, -30, 9), (12, -30, 9)])}
    meshes = [o for o in bpy.data.objects if o.type == 'MESH']
    chk(not any(DEFAULT.match(o.name) for o in bpy.data.objects), "Nessun nome di default (Cube, Cylinder.001, Plane...)",
        "Nomi di default ancora presenti: " + ", ".join(o.name for o in bpy.data.objects if DEFAULT.match(o.name))[:100])
    scn = bpy.data.collections.get("Scena")
    tipi = {o.type for o in scn.objects} if scn else set()
    chk(scn and {'CAMERA', 'LIGHT', 'MESH'} <= tipi, "Collezione 'Scena' con camera, luce e pavimento", "La collezione 'Scena' manca o non contiene camera, luce e pavimento")
    for nome, (cxy, centri) in CL.items():
        coll = bpy.data.collections.get(nome)
        if coll is None: chk(False, "", f"{nome}: collezione '{nome}' non trovata"); continue
        root = bpy.data.objects.get(nome + "_ROOT")
        gruppo = [o for o in meshes if (Vector((bbox(o)[0].x + bbox(o)[1].x, bbox(o)[0].y + bbox(o)[1].y)) / 2 - Vector(cxy)).length < 25]
        chk(len(gruppo) == len(centri), f"{nome}: {len(gruppo)} parti nella posizione originale", f"{nome}: trovo {len(gruppo)} parti nella posizione originale (attese {len(centri)}): hai spostato o eliminato oggetti?")
        chk(all(in_coll(o, nome) and len(o.users_collection) == 1 for o in gruppo), f"{nome}: tutte le parti sono nella collezione '{nome}'", f"{nome}: alcune parti non sono (solo) nella collezione '{nome}'")
        ok_root = root is not None and root.type == 'EMPTY' and in_coll(root, nome) and root.parent is None and near(root.matrix_world.translation, (cxy[0], cxy[1], 0), 2)
        chk(ok_root, f"{nome}_ROOT: Empty a terra al centro del gruppo", f"{nome}_ROOT mancante o non corretto (Empty in {nome}, senza genitore, in {cxy[0]}, {cxy[1]}, 0 ± 2 mm)")
        chk(root is not None and all(o.parent == root for o in gruppo), f"{nome}: parti figlie di {nome}_ROOT", f"{nome}: non tutte le parti sono figlie di {nome}_ROOT")
        chk(all(o.name.startswith(nome + "_") for o in gruppo), f"{nome}: nomi con prefisso '{nome}_'", f"{nome}: nomi senza il prefisso '{nome}_': " + ", ".join(o.name for o in gruppo if not o.name.startswith(nome + "_")))
        cs = [ (bbox(o)[0] + bbox(o)[1]) / 2 for o in gruppo ]
        chk(all(any(near(c, ce) for c in cs) for ce in centri), f"{nome}: posizioni delle parti invariate", f"{nome}: la posizione di alcune parti è cambiata (usa Keep Transform nel parenting)")
print(f"\n=== VERIFICA L03 ({'Casetta' if var == 'A' else 'Scena riordinata'}) ===")
for ok, t in res: print(("[OK]     " if ok else "[ERRORE] ") + t)
n = sum(1 for ok, _ in res if ok); print(f"RISULTATO: {n}/{len(res)} controlli -> {'SUPERATA' if n == len(res) else 'NON SUPERATA'}")
