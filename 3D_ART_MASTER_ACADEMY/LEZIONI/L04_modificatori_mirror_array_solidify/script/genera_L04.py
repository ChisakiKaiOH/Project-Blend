"""Genera i materiali della Lezione 4 (Blender 5.0.1). 1 unità Blender = 1 mm.
Uso:  blender -b --factory-startup --python genera_L04.py -- <cartella_materiali> <cartella_tutor>
Crea in <cartella_materiali>: L04_start.blend, L04_stack_sbagliato.blend, L04_riferimento_A.png, L04_riferimento_B.png
Crea in <cartella_tutor>: soluzione_A/B/C.blend (solo per i test del tutor)
"""
import bpy, bmesh, sys, os, math
from mathutils import Vector

out, tut = sys.argv[sys.argv.index("--") + 1: sys.argv.index("--") + 3]
os.makedirs(out, exist_ok=True); os.makedirs(tut, exist_ok=True)
ESS = os.path.join(os.path.dirname(bpy.app.binary_path), "5.0", "datafiles", "assets", "nodes", "geometry_nodes_essentials.blend")

def reset(): bpy.ops.wm.read_factory_settings(use_empty=True)
def guarda(cam, target): cam.rotation_euler = (Vector(target) - cam.location).to_track_quat('-Z', 'Y').to_euler()
def colora(o, rgba):
    m = bpy.data.materials.new("Mat_" + o.name); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = rgba; o.data.materials.append(m)
def scena(cam_loc=(120, -230, 170), target=(0, 0, 10)):
    sc = bpy.context.scene; u = sc.unit_settings; u.system = 'METRIC'; u.scale_length = 0.001; u.length_unit = 'MILLIMETERS'
    bpy.ops.object.light_add(type='SUN', location=(60, -80, 150), rotation=(math.radians(50), 0, math.radians(30)))
    s = bpy.context.active_object; s.name = "Sole"; s.data.energy = 3
    w = bpy.data.worlds.new("Mondo"); w.use_nodes = True; w.node_tree.nodes["Background"].inputs["Color"].default_value = (0.3, 0.3, 0.33, 1); sc.world = w
    bpy.ops.mesh.primitive_plane_add(size=500); p = bpy.context.active_object; p.name = "Pavimento"; colora(p, (0.55, 0.55, 0.55, 1))
    bpy.ops.object.camera_add(location=cam_loc); c = bpy.context.active_object; c.name = "Camera"; guarda(c, target); sc.camera = c
    cs = bpy.data.collections.new("Scena"); sc.collection.children.link(cs)
    for o in (s, p, c):
        for cc in list(o.users_collection): cc.objects.unlink(o)
        cs.objects.link(o)
    cm = bpy.data.collections.new("Modello"); sc.collection.children.link(cm); return cm

def nuovo_oggetto(nome, bm, coll, loc=(0, 0, 0), rgba=(0.8, 0.5, 0.2, 1)):
    me = bpy.data.meshes.new(nome); bm.to_mesh(me); bm.free(); o = bpy.data.objects.new(nome, me); coll.objects.link(o); o.location = loc; colora(o, rgba); return o

def mezza_vaschetta(scale=1.0):
    """Metà (x da -40 a 0) di una vaschetta 80x50x20, aperta in alto e sul piano di specchio; spigoli sciolti eliminati."""
    bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts: v.co = Vector((v.co.x * 40 - 20, v.co.y * 50, v.co.z * 20 + 10)) * scale
    bm.faces.ensure_lookup_table()
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.normal.z > 0.99 or f.normal.x > 0.99], context='FACES')   # 'FACES', non 'FACES_ONLY'
    return bm

def mezza_cornice():
    """Metà sinistra di una cornice 50x40, barre da 6 mm, a Z = 0, normali verso l'alto."""
    xs, ys = [-25, -19, 0], [-20, -14, 14, 20]
    bm = bmesh.new(); V = [[bm.verts.new((x, y, 0)) for y in ys] for x in xs]
    for i in range(2):
        for j in range(3):
            if i == 1 and j == 1: continue            # foro
            bm.faces.new((V[i][j], V[i + 1][j], V[i + 1][j + 1], V[i][j + 1]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return bm

def array_nuovo(o, count, offset_x):
    if "Array" not in bpy.data.node_groups:
        with bpy.data.libraries.load(ESS, link=False) as (src, dst): dst.node_groups = ["Array"]
    ng = bpy.data.node_groups["Array"]; m = o.modifiers.new("Array", 'NODES'); m.node_group = ng
    sid = {i.name: i.identifier for i in ng.interface.items_tree if getattr(i, 'in_out', None) == 'INPUT'}
    m[sid["Count"]] = count; m[sid["Offset"]] = (offset_x, 0.0, 0.0); return m

def stack(o, solid_t, offset=-1, array=None, ordine="MSA", even=True, merge=True):
    for k in ordine:
        if k == "M":
            m = o.modifiers.new("Mirror", 'MIRROR'); m.use_axis[0] = True; m.use_mirror_merge = merge; m.merge_threshold = 0.01
        elif k == "S":
            m = o.modifiers.new("Solidify", 'SOLIDIFY'); m.thickness = solid_t; m.offset = offset; m.use_even_offset = even
        elif k == "A" and array: array_nuovo(o, *array)

def render(path, res=(1400, 700)):
    sc = bpy.context.scene; sc.render.engine = 'BLENDER_EEVEE'; sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.filepath = path; bpy.ops.render.render(write_still=True)

# ---------- file di partenza ----------
reset(); scena(); bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L04_start.blend"))

# ---------- soluzione A: vaschetta (Mirror -> Solidify -> Array) ----------
reset(); cm = scena(cam_loc=(90, -380, 230), target=(90, 0, 0))
o = nuovo_oggetto("Vaschetta", mezza_vaschetta(), cm, rgba=(0.9, 0.55, 0.2, 1)); stack(o, 2.0, array=(3, 1.125))
render(os.path.join(out, "L04_riferimento_A.png")); bpy.ops.wm.save_as_mainfile(filepath=os.path.join(tut, "soluzione_A.blend"), copy=True)

# ---------- soluzione B: cornice ----------
reset(); cm = scena(cam_loc=(60, -250, 190), target=(60, 0, 0))
o = nuovo_oggetto("Cornice", mezza_cornice(), cm, rgba=(0.3, 0.6, 0.9, 1)); stack(o, 3.0, offset=1, array=(3, 1.2))
render(os.path.join(out, "L04_riferimento_B.png")); bpy.ops.wm.save_as_mainfile(filepath=os.path.join(tut, "soluzione_B.blend"), copy=True)

# ---------- Parte C: tre vaschette con tre errori diversi ----------
reset(); cm = scena(cam_loc=(150, -240, 180), target=(0, 0, 10))
o1 = nuovo_oggetto("Vaschetta_1", mezza_vaschetta(), cm, (0, -80, 0), (0.9, 0.4, 0.4, 1)); stack(o1, 2.0, ordine="SM")                 # ordine sbagliato
o2 = nuovo_oggetto("Vaschetta_2", mezza_vaschetta(scale=2.0), cm, (0, 0, 0), (0.4, 0.9, 0.4, 1)); o2.scale = (0.5, 0.5, 0.5); stack(o2, 2.0)  # scala non applicata
o3 = nuovo_oggetto("Vaschetta_3", mezza_vaschetta(), cm, (0, 80, 0), (0.4, 0.4, 0.9, 1)); stack(o3, 2.0, merge=False)                 # Mirror senza Merge
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L04_stack_sbagliato.blend"))
# soluzione C
for o in (o1, o2, o3):
    if o.name == "Vaschetta_1":
        o.modifiers.move(from_index=1, to_index=0)
    if o.name == "Vaschetta_2":
        bpy.ops.object.select_all(action='DESELECT'); o.select_set(True); bpy.context.view_layer.objects.active = o
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if o.name == "Vaschetta_3": o.modifiers["Mirror"].use_mirror_merge = True
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(tut, "soluzione_C.blend"), copy=True)
print("GENERA_L04_OK")
