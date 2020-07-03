import ctypes

from openfbx.structs.Allocator import Allocator
from openfbx.structs.AnimationStackImpl import AnimationStackImpl
from openfbx.structs.DataView import DataView
from openfbx.structs.Element import Element
from openfbx.structs.MeshImpl import MeshImpl
from openfbx.structs.Object import Object
from openfbx.structs.GlobalSettings import GlobalSettings
from openfbx.structs.TakeInfo import TakeInfo
from openfbx.structs.interfaces.IScene import IScene
from openfbx.structs.Root import Root
from openfbx.structs.Video import Video
from openfbx.structs.abstract.AnimationStack import AnimationStack
from openfbx.structs.abstract.Mesh import Mesh


class Scene(IScene):
    class Connection(ctypes.Structure):
        class Type(ctypes.Structure):
            _fields_ = [
                ("OBJECT_OBJECT", ctypes.c_int),
                ("OBJECT_PROPERTY", ctypes.c_int)
            ]

        class ObjectPair(ctypes.Structure):
            _fields_ = [
                ("element", ctypes.POINTER(Element)),
                ("object", ctypes.POINTER(Object))
            ]

        _fields_ = [
            ("type", Type),
            ("from", ctypes.c_uint64),
            ("to", ctypes.c_uint64),
            ("property", DataView)
        ]

    _fields_ = IScene._fields_ + [
        ("m_root_element", ctypes.POINTER(Element)),
        ("m_root", ctypes.POINTER(Root)),
        ("m_scene_frame_rate", ctypes.c_float),
        ("m_settings", GlobalSettings),
        #("m_object_map", ),
        ("m_all_objects", ctypes.POINTER(Object) * 1),
        ("m_meshes", ctypes.POINTER(MeshImpl) * 1),
        ("m_animation_stacks", ctypes.POINTER(AnimationStackImpl) * 1),
        ("m_connections", Connection * 1),
        ("m_data", ctypes.c_uint8 * 1),
        ("m_take_infos", TakeInfo * 1),
        ("m_videos", Video * 1),
        ("m_allocator", Allocator)
    ]