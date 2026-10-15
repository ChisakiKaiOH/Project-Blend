"""Genera i materiali della Lezione 5 (Blender 5.0.1). 1 unità Blender = 1 mm.
Uso:  blender -b --factory-startup --python genera_L05.py -- <cartella_materiali> <cartella_tutor>
Crea in <cartella_materiali>: L05_start.blend, L05_blocchi_sbagliati.blend, L05_riferimento_A.png, L05_riferimento_B.png
Crea in <cartella_tutor>: soluzione_A/B/C.blend (solo per i test del tutor)
"""
import bpy, bmesh, sys, os, math
from mathutils import Vector

out, tut = sys.argv[sys.argv.index("--") + 1: sys.argv.index("--") + 3]
os.makedirs(out, exist_ok=True); os.makedirs(tut, exist_ok=True)

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

def nuovo_oggetto(nome, bm, coll, loc=(0, 0, 0), rgba=(0.8, 0.5, 0.2, 1), smooth=True):
    me = bpy.data.meshes.new(nome); bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth = smooth
    o = bpy.data.objects.new(nome, me); coll.objects.link(o); o.location = loc; colora(o, rgba); return o

def scatola(dx, dy, dz, inset=None, crease=None):
    bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts: v.co = Vector((v.co.x * dx, v.co.y * dy, v.co.z * dz))
    if inset: bmesh.ops.inset_individual(bm, faces=bm.faces[:], thickness=inset, use_even_offset=True)
    if crease is not None:
        cl = bm.edges.layers.float.new("crease_edge")
        for e in bm.edges: e[cl] = crease
    return bm

def sapone_bm():
    """Scatola 80x50x20 con supporti a 3 mm dai bordi, incavo 50x20 (pareti a x=±25, y=±10) profondo 1,5 mm sulla faccia superiore, con supporti."""
    bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts: v.co = Vector((v.co.x * 80, v.co.y * 50, v.co.z * 20))
    bm.faces.ensure_lookup_table()
    # supporti sui bordi: inset individuale su tutte le facce
    r = bmesh.ops.inset_individual(bm, faces=bm.faces[:], thickness=3.0, use_even_offset=True)
    top = max(bm.faces, key=lambda f: f.calc_center_median().z if abs(f.normal.z - 1) < 1e-3 else -1e9)
    # faccia superiore interna 74x44: inset 10,5 -> 53x23 (anello di supporto), poi inset 1,5 -> 50x20 (bordo dell'incavo)
    bmesh.ops.inset_region(bm, faces=[top], thickness=10.5, use_even_offset=True)
    bmesh.ops.inset_region(bm, faces=[top], thickness=1.5, use_even_offset=True)
    ext = bmesh.ops.extrude_discrete_faces(bm, faces=[top])["faces"][0]
    bmesh.ops.translate(bm, verts=ext.verts, vec=Vector((0, 0, -1.5)))
    bmesh.ops.inset_region(bm, faces=[ext], thickness=1.5, use_even_offset=True)           # supporto sul fondo
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return bm

def sub(o, lv=2, rl=3):
    m = o.modifiers.new("Subdivision", 'SUBSURF'); m.levels = lv; m.render_levels = rl; return m

def render(path, res=(1400, 700)):
    sc = bpy.context.scene; sc.render.engine = 'BLENDER_EEVEE'; sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.filepath = path; bpy.ops.render.render(write_still=True)

# ---------- file di partenza ----------
reset(); scena(); bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L05_start.blend"))

# ---------- soluzione A: blocco 40 con supporti a 4 mm ----------
reset(); cm = scena(cam_loc=(70, -130, 90), target=(0, 0, 20))
o = nuovo_oggetto("Blocco", scatola(40, 40, 40, inset=4), cm, (0, 0, 20), (0.9, 0.55, 0.2, 1)); sub(o)
render(os.path.join(out, "L05_riferimento_A.png")); bpy.ops.wm.save_as_mainfile(filepath=os.path.join(tut, "soluzione_A.blend"), copy=True)

# ---------- soluzione B: sapone ----------
reset(); cm = scena(cam_loc=(60, -150, 130), target=(0, 0, 8))
o = nuovo_oggetto("Sapone", sapone_bm(), cm, (0, 0, 10), (0.3, 0.7, 0.8, 1)); sub(o)
render(os.path.join(out, "L05_riferimento_B.png")); bpy.ops.wm.save_as_mainfile(filepath=os.path.join(tut, "soluzione_B.blend"), copy=True)

# ---------- Parte C: tre blocchi con tre errori ----------
reset(); cm = scena(cam_loc=(0, -230, 150), target=(0, 0, 20))
o1 = nuovo_oggetto("Blocco_1", scatola(40, 40, 40), cm, (-70, 0, 20), (0.9, 0.4, 0.4, 1)); sub(o1)                                  # nessun supporto
o2 = nuovo_oggetto("Blocco_2", scatola(40, 40, 40, inset=4, crease=1.0), cm, (0, 0, 20), (0.4, 0.9, 0.4, 1)); sub(o2)               # crease 1 ovunque
o3 = nuovo_oggetto("Blocco_3", scatola(40, 40, 40, inset=4), cm, (70, 0, 20), (0.4, 0.4, 0.9, 1), smooth=False); sub(o3)             # ombreggiatura flat
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L05_blocchi_sbagliati.blend"))

# ---------- file obiettivo per la Parte B: scena di partenza + sapone finito (mesh già valutata, senza modificatore) ----------
reset(); cm = scena(cam_loc=(60, -150, 130), target=(60, 0, 8))
tmp = nuovo_oggetto("tmp", sapone_bm(), cm, (0, 0, 10)); sub(tmp)
dg = bpy.context.evaluated_depsgraph_get(); me2 = bpy.data.meshes.new_from_object(tmp.evaluated_get(dg), depsgraph=dg)
bpy.data.objects.remove(tmp)
for p in me2.polygons: p.use_smooth = True
me2.name = "Obiettivo_Sapone"
co = bpy.data.collections.new("Obiettivo"); bpy.context.scene.collection.children.link(co)
ob = bpy.data.objects.new("Obiettivo_Sapone", me2); co.objects.link(ob); ob.location = (120, 0, 10); colora(ob, (0.3, 0.8, 0.5, 1))
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L05_obiettivo_B.blend"))
