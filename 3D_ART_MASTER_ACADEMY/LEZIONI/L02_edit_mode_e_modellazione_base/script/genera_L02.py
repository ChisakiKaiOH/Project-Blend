"""Genera i materiali della Lezione 2 (Blender 5.0.1).
Uso:  blender -b --factory-startup --python genera_L02.py -- <cartella_materiali> <cartella_riferimenti_tutor>
Crea in <cartella_materiali>: L02_start.blend, L02_mesh_difettosa.blend, L02_riferimento_A.png, L02_riferimento_B.png
Crea in <cartella_riferimenti_tutor>: soluzione_A.blend, soluzione_B.blend (soluzioni di prova, solo per i test del tutor)
"""
import bpy, bmesh, sys, os, math
from mathutils import Vector

out, tut = sys.argv[sys.argv.index("--") + 1: sys.argv.index("--") + 3]
os.makedirs(out, exist_ok=True); os.makedirs(tut, exist_ok=True)

def scena():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.object.light_add(type='SUN', location=(5, -5, 8), rotation=(math.radians(50), 0, math.radians(30)))
    bpy.context.active_object.name = "Sole"; bpy.context.active_object.data.energy = 3
    w = bpy.data.worlds.new("Mondo"); w.use_nodes = True
    w.node_tree.nodes["Background"].inputs["Color"].default_value = (0.25, 0.25, 0.28, 1)
    bpy.context.scene.world = w
    bpy.ops.mesh.primitive_plane_add(size=6); bpy.context.active_object.name = "Pavimento"
    bpy.ops.object.camera_add(location=(2.2, -2.6, 1.6), rotation=(math.radians(68), 0, math.radians(40)))
    bpy.context.active_object.name = "Camera"; bpy.context.scene.camera = bpy.context.active_object

def colora(o, rgba):
    m = bpy.data.materials.new("Mat_" + o.name); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = rgba
    o.data.materials.append(m)

def cubo(nome, pos, rgba):
    bpy.ops.mesh.primitive_cube_add(size=2, location=pos); o = bpy.context.active_object
    o.name = nome; colora(o, rgba); return o

def costruisci_tavolo(nome, dx, dy, h, spess, gamba, pos, rgba):
    """Costruisce un tavolo con la stessa logica didattica: piano + 4 gambe estruse dalle facce d'angolo."""
    me = bpy.data.meshes.new(nome); o = bpy.data.objects.new(nome, me); bpy.context.collection.objects.link(o)
    bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts: v.co = Vector((v.co.x * dx, v.co.y * dy, v.co.z * spess))
    # "loop cut": 2 tagli per direzione, a distanza 'gamba' dal bordo
    for no, co in ((Vector((1, 0, 0)), Vector((dx / 2 - gamba, 0, 0))), (Vector((1, 0, 0)), Vector((-dx / 2 + gamba, 0, 0))),
                   (Vector((0, 1, 0)), Vector((0, dy / 2 - gamba, 0))), (Vector((0, 1, 0)), Vector((0, -dy / 2 + gamba, 0)))):
        g = bm.verts[:] + bm.edges[:] + bm.faces[:]
        bmesh.ops.bisect_plane(bm, geom=g, plane_co=co, plane_no=no)
    bm.faces.ensure_lookup_table()
    zmin = -spess / 2
    corner = [f for f in bm.faces if f.normal.z < -0.99 and abs(f.calc_center_median().z - zmin) < 1e-6
              and abs(abs(f.calc_center_median().x) - (dx / 2 - gamba / 2)) < 1e-4 and abs(abs(f.calc_center_median().y) - (dy / 2 - gamba / 2)) < 1e-4]
    assert len(corner) == 4, len(corner)
    r = bmesh.ops.extrude_face_region(bm, geom=corner)
    nv = [e for e in r["geom"] if isinstance(e, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, verts=nv, vec=Vector((0, 0, -(h - spess))))
    bmesh.ops.delete(bm, geom=corner, context='FACES_ONLY')   # le facce originali restano dentro il solido: vanno eliminate
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me); bm.free()
    o.location = (pos[0], pos[1], h - spess / 2)    # base appoggiata a Z=0
    colora(o, rgba); return o

# --- file di partenza ---
scena()
cubo("Sgabello", (-1.8, 0, 1), (0.9, 0.55, 0.2, 1)); cubo("Tavolino", (1.8, 0, 1), (0.3, 0.6, 0.9, 1))
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L02_start.blend"))

# --- mesh difettosa (Parte C) ---
scena()
bpy.ops.object.select_all(action='DESELECT')
me = bpy.data.meshes.new("Difettoso"); o = bpy.data.objects.new("Difettoso", me); bpy.context.collection.objects.link(o)
bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0); bm.faces.ensure_lookup_table()
top = [f for f in bm.faces if f.normal.z > 0.99][0]; bmesh.ops.delete(bm, geom=[top], context='FACES_ONLY')   # buco in alto
front = [f for f in bm.faces if f.normal.y < -0.99][0]; front.normal_flip()                               # normale invertita sul lato -Y
bm.verts.new((0.9, 0.9, 0.0)); bm.verts.new((-0.9, 0.9, 0.3))                                             # 2 vertici sciolti
bm.to_mesh(me); bm.free(); o.location = (0, 0, 0.5); colora(o, (0.8, 0.8, 0.8, 1))
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L02_mesh_difettosa.blend"))

# --- soluzioni di riferimento (solo tutor) + immagini di riferimento ---
sc = bpy.context.scene; sc.render.engine = 'BLENDER_EEVEE'; sc.render.resolution_x = 900; sc.render.resolution_y = 600
RIF = {"A": ("Sgabello", 0.30, 0.30, 0.45, 0.03, 0.10, (0, 0), (0.9, 0.55, 0.2, 1)),
       "B": ("Tavolino", 0.60, 0.40, 0.45, 0.03, 0.04, (0, 0), (0.3, 0.6, 0.9, 1))}
for k, (nome, dx, dy, h, sp, g, pos, col) in RIF.items():
    scena(); costruisci_tavolo(nome, dx, dy, h, sp, g, pos, col)
    sc = bpy.context.scene; sc.render.engine = 'BLENDER_EEVEE'; sc.render.resolution_x = 900; sc.render.resolution_y = 600
    cam = bpy.data.objects["Camera"]; cam.location = (0.9, -1.0, 0.7) if k == "A" else (1.5, -1.7, 1.1)
    cam.rotation_euler = [math.radians(a) for a in (70, 0, 41)]
    bpy.data.objects["Pavimento"].location = (0, 0, 0)
    sc.render.filepath = os.path.join(out, f"L02_riferimento_{k}.png"); bpy.ops.render.render(write_still=True)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(tut, f"soluzione_{k}.blend"), copy=True)
print("GENERA_L02_OK")
