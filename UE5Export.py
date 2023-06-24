bl_info = {
    "name": "UE5_Exporter",
    "blender": (3, 40, 0),
    "category": "Object",
  "description": "UE5エクスポートアドオン",
  "author": "kunu",
}

import bpy
import os

class UE_PT_ExportPanel(bpy.types.Panel):
    bl_label = "UE5Exporter"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        layout.prop(context.object, "out_dir")
        layout.operator("object.export_fbx")


class ExportUEOperator(bpy.types.Operator):
    bl_idname = "object.export_fbx"
    bl_label = "Export FBX"

    def execute(self, context):
        
        obj_name = bpy.context.object.name
        dir_path = bpy.context.object.out_dir
        filepath = os.path.basename(bpy.data.filepath).split(".")[0]

        if dir_path == "":
            raise ValueError("ファイルを保存してください！")

        out_path = os.path.join(dir_path, filepath + obj_name) + ".fbx"

        bpy.ops.export_scene.fbx(filepath=out_path, 
                                 check_existing=False, 
                                 use_selection=True, 
                                 use_visible=False, 
                                 use_active_collection=False, 
                                 global_scale=1.0,
                                 apply_unit_scale=True, 
                                 apply_scale_options='FBX_SCALE_NONE', 
                                 use_space_transform=True, 
                                 bake_space_transform=False, 
                                 object_types={'MESH'}, 
                                 use_mesh_modifiers=True, 
                                 use_mesh_modifiers_render=False, 
                                 mesh_smooth_type='OFF', 
                                 colors_type='SRGB', 
                                 prioritize_active_color=False, 
                                 use_subsurf=False, 
                                 use_mesh_edges=False, 
                                 use_tspace=False, 
                                 use_triangles=True, 
                                 use_custom_props=False, 
                                 add_leaf_bones=False, 
                                 primary_bone_axis='Y', 
                                 secondary_bone_axis='X', 
                                 use_armature_deform_only=False, 
                                 armature_nodetype='NULL', 
                                 bake_anim=False, 
                                #  bake_anim_use_all_bones=True, 
                                #  bake_anim_use_nla_strips=True, 
                                #  bake_anim_use_all_actions=True, 
                                #  bake_anim_force_startend_keying=True, 
                                #  bake_anim_step=1.0,
                                #  bake_anim_simplify_factor=1.0, 
                                 path_mode='AUTO', 
                                 embed_textures=False, 
                                 batch_mode='OFF', 
                                 use_batch_own_dir=True, 
                                 use_metadata=True, 
                                 axis_forward='-Z', 
                                 axis_up='Y'
                                 )
        self.report({'INFO'}, f"Saved to: {out_path}")
        
        return {'FINISHED'}


def register():
    bpy.types.Object.out_dir = bpy.props.StringProperty(
        name="Outdir",
        description="out dir",
        default="C:/temps/"
    )

    bpy.utils.register_class(UE_PT_ExportPanel)
    bpy.utils.register_class(ExportUEOperator)


def unregister():
    bpy.utils.unregister_class(UE_PT_ExportPanel)
    bpy.utils.unregister_class(ExportUEOperator)

    del bpy.types.Object.out_dir

if __name__ == "__main__":
    register()
