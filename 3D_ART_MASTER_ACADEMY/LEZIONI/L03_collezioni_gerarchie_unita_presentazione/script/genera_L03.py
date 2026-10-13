"""Genera i materiali della Lezione 3 (Blender 5.0.1). 1 unità Blender = 1 mm nei file didattici.
Uso:  blender -b --factory-startup --python genera_L03.py -- <cartella_materiali> <cartella_tutor>
Crea in <cartella_materiali>: L03_start.blend, L03_scena_disordinata.blend, L03_mesh_diagnosi.blend, L03_riferimento_casetta.png
Crea in <cartella_tutor>: soluzione_A/B/C.blend (solo per i test del tutor)
"""
import bpy, bmesh, sys, os, math
from mathutils import Vector, Matrix

out, tut = sys.argv[sys.argv.index("--") + 1: sys.argv.index("--") + 3]
os.makedirs(out, exist_ok=True); os.makedirs(tut, exist_ok=True)

def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def colora(o, rgba):
    m = bpy.data.materials.new("Mat_" + o.name); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = rgba
    o.data.materials.append(m)

def guarda(cam, target):
    d = Vector(target) - cam.location
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

def scena_base(nomi_it=False):
    """Camera, sole e pavimento (200 x 200 mm)."""
    bpy.ops.object.light_add(type='SUN', location=(60, -80, 120), rotation=(math.radians(50), 0, math.radians(30)))
    s = bpy.context.active_object; s.name = "Sole" if nomi_it else "Sun"; s.data.energy = 3
    w = bpy.data.worlds.new("Mondo"); w.use_nodes = True
    w.node_tree.nodes["Background"].inputs["Color"].default_value = (0.3, 0.3, 0.33, 1); bpy.context.scene.world = w
    bpy.ops.mesh.primitive_plane_add(size=200); p = bpy.context.active_object; p.name = "Pavimento" if nomi_it else "Plane"
    colora(p, (0.55, 0.55, 0.55, 1))
    bpy.ops.object.camera_add(location=(150, -175, 115)); c = bpy.context.active_object; c.name = "Camera"
    guarda(c, (0, 0, 30)); bpy.context.scene.camera = c

def box(nome, dim, centro, rgba):
    bpy.ops.mesh.primitive_cube_add(size=1, location=centro); o = bpy.context.active_object; o.name = nome
    o.scale = dim; bpy.ops.object.transform_apply(location=False, rotation=False, scale=True); colora(o, rgba); return o

def impostazioni_mm(sc):
    u = sc.unit_settings; u.system = 'METRIC'; u.scale_length = 0.001; u.length_unit = 'MILLIMETERS'

def casa():
    """Soluzione di riferimento della Parte A."""
    corpo = box("Casa_Corpo", (60, 40, 40), (0, 0, 20), (0.85, 0.75, 0.6, 1))
    # tetto a capanna: lastra 66x46x10, colmo = spigolo centrale superiore alzato di 10
    t = box("Casa_Tetto", (66, 46, 10), (0, 0, 45), (0.6, 0.2, 0.15, 1))
    bm = bmesh.new(); bm.from_mesh(t.data)
    bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, 0), plane_no=(0, 1, 0))
    for v in bm.verts:
        if abs(v.co.y) < 1e-6 and v.co.z > 0: v.co.z += 10
    bm.to_mesh(t.data); bm.free()
    porta = box("Casa_Porta", (12, 2, 22), (0, -20, 11), (0.35, 0.2, 0.1, 1))
    camino = box("Casa_Camino", (8, 8, 20), (-20, 10, 58), (0.5, 0.5, 0.5, 1))
    root = bpy.data.objects.new("Casa_ROOT", None); bpy.context.collection.objects.link(root); root.empty_display_size = 20
    for p in (corpo, t, porta, camino):
        p.parent = root
    return root, (corpo, t, porta, camino)

def collezioni(sc, assegna):
    """assegna: {nome_collezione: [oggetti]} -> sposta gli oggetti, creando le collezioni."""
    for nome, objs in assegna.items():
        c = bpy.data.collections.new(nome); sc.collection.children.link(c)
        for o in objs:
            for cc in list(o.users_collection): cc.objects.unlink(o)
            c.objects.link(o)

# ---------- Parte A: file di partenza ----------
reset(); scena_base(nomi_it=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L03_start.blend"))

# ---------- soluzione A + immagine di riferimento ----------
reset(); scena_base(nomi_it=True); sc = bpy.context.scene; impostazioni_mm(sc)
root, parti = casa()
scene_objs = [o for o in bpy.data.objects if o.name in ("Camera", "Sole", "Pavimento")]
ref = bpy.data.objects.new("Rif_Casetta", None); ref.empty_display_type = 'IMAGE'
collezioni(sc, {"Casa": [root, *parti], "Scena": scene_objs, "Riferimenti": [ref]})
sc.render.engine = 'BLENDER_EEVEE'; sc.render.resolution_x = 1600; sc.render.resolution_y = 900
sc.render.filepath = os.path.join(out, "L03_riferimento_casetta.png"); bpy.ops.render.render(write_still=True)
img = bpy.data.images.load(os.path.join(out, "L03_riferimento_casetta.png")); ref.data = img
sc.render.filepath = os.path.join(tut, "L03_casetta_render_v01.png"); bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(tut, "soluzione_A.blend"), copy=True)

# ---------- Parte B: scena disordinata ----------
CL = {  # cluster: (centro xy, oggetti (tipo, dimensioni/param, centro, colore))
    "Albero": ((-40, 30), [("cyl", (3, 20), (-40, 30, 10), (0.4, 0.25, 0.1, 1)), ("cone", (12, 30), (-40, 30, 35), (0.15, 0.5, 0.2, 1))]),
    "Lampione": ((40, 25), [("cyl", (4, 4), (40, 25, 2), (0.2, 0.2, 0.2, 1)), ("cyl", (1.5, 40), (40, 25, 24), (0.25, 0.25, 0.25, 1)), ("sph", (5,), (40, 25, 48), (1, 0.9, 0.5, 1))]),
    "Panchina": ((0, -30), [("box", (30, 10, 2), (0, -30, 20), (0.5, 0.3, 0.15, 1)), ("box", (2, 10, 18), (-12, -30, 9), (0.3, 0.3, 0.3, 1)), ("box", (2, 10, 18), (12, -30, 9), (0.3, 0.3, 0.3, 1))]),
}
def crea_prim(tipo, p, c, rgba):
    if tipo == "cyl": bpy.ops.mesh.primitive_cylinder_add(radius=p[0], depth=p[1], location=c)
    elif tipo == "cone": bpy.ops.mesh.primitive_cone_add(radius1=p[0], depth=p[1], location=c)
    elif tipo == "sph": bpy.ops.mesh.primitive_uv_sphere_add(radius=p[0], location=c)
    else:
        bpy.ops.mesh.primitive_cube_add(size=1, location=c); bpy.context.active_object.scale = p; bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o = bpy.context.active_object; colora(o, rgba); return o
reset(); scena_base(nomi_it=False)
import random; random.seed(7); lista = [(k, d) for k, (cxy, ds) in CL.items() for d in ds]; random.shuffle(lista)
for k, d in lista: crea_prim(*d)    # nomi di default: Cube, Cylinder.001 ...
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L03_scena_disordinata.blend"))
# soluzione B
bpy.ops.wm.open_mainfile(filepath=os.path.join(out, "L03_scena_disordinata.blend")); sc = bpy.context.scene; impostazioni_mm(sc)
meshes = [o for o in bpy.data.objects if o.type == 'MESH' and o.name != "Plane"]
assegna = {"Scena": [bpy.data.objects["Camera"], bpy.data.objects["Sun"], bpy.data.objects["Plane"]]}
bpy.data.objects["Plane"].name = "Pavimento"; bpy.data.objects["Sun"].name = "Sole"
for k, (cxy, ds) in CL.items():
    root = bpy.data.objects.new(k + "_ROOT", None); bpy.context.collection.objects.link(root); root.location = (cxy[0], cxy[1], 0)
    ms = sorted([o for o in meshes if (Vector((o.location.x, o.location.y)) - Vector(cxy)).length < 20], key=lambda o: o.location.z)
    for i, o in enumerate(ms):
        o.name = f"{k}_Parte{i+1}"; o.parent = root; o.matrix_parent_inverse = Matrix.Translation((-cxy[0], -cxy[1], 0))   # equivale a 'Keep Transform'
    assegna[k] = [root, *ms]
collezioni(sc, assegna)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(tut, "soluzione_B.blend"), copy=True)

# ---------- Parte C: tre mesh difettose ----------
reset(); scena_base(nomi_it=True)
def mesh_obj(nome, bm, loc, rgba):
    me = bpy.data.meshes.new(nome); bm.to_mesh(me); bm.free(); o = bpy.data.objects.new(nome, me); bpy.context.collection.objects.link(o); o.location = loc; colora(o, rgba); return o
# A: tutte le normali invertite
bm = bmesh.new(); bmesh.ops.create_cube(bm, size=20); bmesh.ops.reverse_faces(bm, faces=bm.faces); mesh_obj("Oggetto_A", bm, (-40, 0, 10), (0.8, 0.3, 0.3, 1))
# B: faccia interna che divide il cubo in due
bm = bmesh.new(); bmesh.ops.create_cube(bm, size=20)
bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, 0), plane_no=(1, 0, 0))
mid = [v for v in bm.verts if abs(v.co.x) < 1e-6]; bm.verts.ensure_lookup_table()
cx = Vector((0, 0, 0)); mid.sort(key=lambda v: math.atan2(v.co.z, v.co.y)); bm.faces.new(mid)
mesh_obj("Oggetto_B", bm, (0, 0, 10), (0.3, 0.8, 0.3, 1))
# C: sei facce separate (vertici doppi)
bm = bmesh.new(); bmesh.ops.create_cube(bm, size=20); bmesh.ops.split_edges(bm, edges=bm.edges[:]); mesh_obj("Oggetto_C", bm, (40, 0, 10), (0.3, 0.3, 0.8, 1))
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L03_mesh_diagnosi.blend"))
# soluzione C
for o in [bpy.data.objects[n] for n in ("Oggetto_A", "Oggetto_B", "Oggetto_C")]:
    bm = bmesh.new(); bm.from_mesh(o.data)
    if o.name == "Oggetto_B":
        bmesh.ops.delete(bm, geom=[f for f in bm.faces if all(abs(v.co.x) < 1e-6 for v in f.verts)], context='FACES_ONLY')
    if o.name == "Oggetto_C": bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces); bm.to_mesh(o.data); bm.free()
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(tut, "soluzione_C.blend"), copy=True)
print("GENERA_L03_OK")
