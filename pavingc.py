bl_info = {
    "name": "Paving 64",
    "author": "Victor Butyrin (publius)",
    "version": (1, 5, 1),
    "blender": (2, 69, 0),
    "location": "View3D > Add > Mesh",
    "description": "Create Cold War Assault 9.92 sq.km terrain",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Add Mesh"}

import bpy

def makeVertices(wsd, elevation):
	vertices = []
	z = elevation * 0.01
	for y in range(wsd):
		for x in range(wsd):
			vertices.append((x * 0.5, y * 0.5, z))
	return vertices

def makeFaces(wsd):
	faces = []
	limit = wsd * (wsd - 1)
	count = wsd - 1
	for co in range(limit):
		if count > 0:
			lb = co
			lt = wsd + lb
			rt = lt + 1
			rb = lb + 1
			faces.append((lb, lt, rt, rb))
			count -= 1
		else:
			count = wsd - 1
	return faces

def createObject(name, vertices, faces):
	me = bpy.data.meshes.new(name)
	ob = bpy.data.objects.new(name, me)
	bpy.context.scene.objects.link(ob)
	me.from_pydata(vertices, [], faces)
	me.update()
	return ob

class PavingCOperator(bpy.types.Operator):
	'''Paving 63 x 63 CWA terrain'''
	bl_idname = 'mesh.add_64_object'
	bl_label = 'Paving 9.92 square kilometers'
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		createObject('Terrain', makeVertices(64, -27), makeFaces(64))
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(PavingCOperator.bl_idname, icon = 'GRID')

def register():
	bpy.utils.register_class(PavingCOperator)
	bpy.types.INFO_MT_mesh_add.append(menu_func)

def unregister():
	bpy.utils.unregister_class(PavingCOperator)
	bpy.types.INFO_MT_mesh_add.remove(menu_func)

if __name__ == '__main__':
	register()
