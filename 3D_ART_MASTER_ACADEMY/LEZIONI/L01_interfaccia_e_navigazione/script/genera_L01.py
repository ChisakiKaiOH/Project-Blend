"""Genera i materiali della Lezione 1 (Blender 5.0.1).
Uso:  blender -b --factory-startup --python genera_L01.py -- <cartella_output> <cartella_json>
Crea in <cartella_output>: L01_start.blend, L01_A_fronte.png, L01_A_alto.png, L01_B_destra.png, L01_B_alto.png
Crea in <cartella_json>:  L01_target_A.json, L01_target_B.json, L01_target_C.json  (valori attesi per verifica_L01.py)
La soluzione NON viene salvata nel repository: serve solo a calcolare le misure.
"""
import bpy, sys, os, math, json
from mathutils import Vector

out, jdir = sys.argv[sys.argv.index("--") + 1: sys.argv.index("--") + 3]
os.makedirs(out, exist_ok=True); os.makedirs(jdir, exist_ok=True)

TIPI = {"Cubo": "cube", "Cono": "cone", "Cilindro": "cylinder", "Sfera": "sphere", "Toro": "torus"}
PARTENZA = {"Cubo": (-3, 2.5), "Cono": (1.5, -3), "Cilindro": (0.5, 3), "Sfera": (-1, -2), "Toro": (3.5, 1.5)}
COLORI = {"Cubo": (0.8, 0.2, 0.2, 1), "Cono": (0.2, 0.6, 0.9, 1), "Cilindro": (0.9, 0.7, 0.1, 1),
          "Sfera": (0.3, 0.8, 0.4, 1), "Toro": (0.7, 0.3, 0.8, 1)}
# loc, rot (gradi), scala
LAYOUT = {
    "A": {  # guidata: fila lungo X
        "Cubo": ((-4, 0, 1), (0, 0, 0), (1, 1, 1)), "Cono": ((-2, 0, 1), (180, 0, 0), (1, 1, 1)),
        "Cilindro": ((0, 0, 1.5), (0, 0, 0), (0.5, 0.5, 1.5)), "Sfera": ((2, 0, 1), (0, 0, 0), (1, 1, 1)),
        "Toro": ((4, 0, 1.25), (90, 0, 0), (1, 1, 1))},
    "B": {  # autonoma: fila lungo Y, ordine, rotazioni e scale diversi
        "Toro": ((0, -4, 0.25), (0, 0, 0), (1, 1, 1)), "Sfera": ((0, -2, 0.5), (0, 0, 0), (0.5, 0.5, 0.5)),
        "Cilindro": ((0, 0, 0.5), (0, 0, 0), (1, 1, 0.5)), "Cono": ((0, 2, 1), (0, 0, 0), (1, 1, 1)),
        "Cubo": ((0, 4, 2), (0, 0, 0), (1, 1, 2))},
}
# C = disposizione B con due rotazioni (verifica del comando R, nessuna immagine di riferimento)
LAYOUT["C"] = dict(LAYOUT["B"])
LAYOUT["C"]["Cono"] = ((0, 2, 1), (180, 0, 0), (1, 1, 1))
LAYOUT["C"]["Toro"] = ((0, -4, 1.25), (90, 0, 0), (1, 1, 1))
VISTE = {  # layout: [(nome file, posizione camera, rotazione gradi, nascondi pavimento)]
    "A": [("L01_A_fronte.png", (0, -15, 1.5), (90, 0, 0), True), ("L01_A_alto.png", (0, 0, 15), (0, 0, 0), False)],
    "B": [("L01_B_destra.png", (15, 0, 1.5), (90, 0, 90), True), ("L01_B_alto.png", (0, 0, 15), (0, 0, 90), False)],
}

def crea(nome):
    {"cube": bpy.ops.mesh.primitive_cube_add, "cone": bpy.ops.mesh.primitive_cone_add,
     "cylinder": bpy.ops.mesh.primitive_cylinder_add, "sphere": bpy.ops.mesh.primitive_uv_sphere_add,
     "torus": bpy.ops.mesh.primitive_torus_add}[TIPI[nome]]()
    o = bpy.context.active_object; o.name = nome
    m = bpy.data.materials.new("Mat_" + nome); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = COLORI[nome]
    o.data.materials.append(m)
    return o

def scena():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.object.light_add(type='SUN', location=(5, -5, 8), rotation=(math.radians(50), 0, math.radians(30)))
    bpy.context.active_object.name = "Sole"; bpy.context.active_object.data.energy = 3
    w = bpy.data.worlds.new("Mondo"); w.use_nodes = True
    w.node_tree.nodes["Background"].inputs["Color"].default_value = (0.25, 0.25, 0.28, 1)
    bpy.context.scene.world = w
    bpy.ops.mesh.primitive_plane_add(size=14); bpy.context.active_object.name = "Pavimento"
    bpy.ops.object.camera_add(location=(8, -10, 6), rotation=(math.radians(65), 0, math.radians(38)))
    bpy.context.active_object.name = "Camera"; bpy.context.scene.camera = bpy.context.active_object

def misure(o):
    vs = [o.matrix_world @ v.co for v in o.data.vertices]
    c = sum(vs, Vector()) / len(vs)
    mn = [min(v[i] for v in vs) for i in range(3)]; mx = [max(v[i] for v in vs) for i in range(3)]
    return {"centro": [round(x, 3) for x in c], "min": [round(x, 3) for x in mn], "max": [round(x, 3) for x in mx]}

scena()
for nome, (x, y) in PARTENZA.items():
    crea(nome).location = (x, y, 1.0)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "L01_start.blend"))

for key, lay in LAYOUT.items():
    for nome, (loc, rot, scl) in lay.items():
        o = bpy.data.objects[nome]; o.location = loc
        o.rotation_euler = [math.radians(a) for a in rot]; o.scale = scl
    bpy.context.view_layer.update()
    json.dump({n: misure(bpy.data.objects[n]) for n in lay}, open(os.path.join(jdir, f"L01_target_{key}.json"), "w"), indent=1)
    sc = bpy.context.scene; sc.render.engine = 'BLENDER_EEVEE'; sc.render.resolution_x = 1000; sc.render.resolution_y = 500
    cam = bpy.data.objects["Camera"]; cam.data.type = 'ORTHO'; cam.data.ortho_scale = 11
    for fn, loc, rot, hide in VISTE.get(key, []):
        cam.location = loc; cam.rotation_euler = [math.radians(a) for a in rot]
        bpy.data.objects["Pavimento"].hide_render = hide
        sc.render.filepath = os.path.join(out, fn); bpy.ops.render.render(write_still=True)
    # salva soluzione solo fuori dal repository, per i test del tutor
    bpy.ops.wm.save_as_mainfile(filepath=f"/tmp/claude-0/s/soluzione_{key}.blend", copy=True)
print("GENERA_L01_OK")
