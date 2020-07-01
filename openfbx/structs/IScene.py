import ctypes
from ctypes import Structure

from openfbx import DLL


class IScene(Structure):
    def get_root_element(self):
        return DLL.ofbx.ISceneGetRootElement()

    def get_root(self):
        return DLL.ofbx.ISceneGetRoot()

    def get_take_info(self, name):
        DLL.ofbx.ISceneGetTakeInfo(ctypes.c_char_p(name))

    def get_mesh_count(self):
        return DLL.ofbx.ISceneGetMeshCount()

    def get_scene_frame_rate(self):
        return DLL.ofbx.ISceneGetSceneFrameRate()

    def get_global_settings(self):
        return DLL.ofbx.ISceneGetGlobalSettings()

    def get_mesh(self, index):
        return DLL.ofbx.ISceneGetMesh(ctypes.c_int(index))

    def get_animation_stack_count(self):
        return DLL.ofbx.ISceneGetAnimationStackCount()

    def get_animation_stack(self, index):
        return DLL.ofbx.ISceneGetAnimationStack(ctypes.c_int(index))

    def get_all_objects(self):
        return DLL.ofbx.ISceneGetAllObjects()

    def get_all_object_count(self):
        return DLL.ofbx.ISceneGetAllObjectCount()
