import ctypes

from openfbx.structs.Object import Object


class Geometry(Object):
    _fields_ = Object._fields_ + [
        ("s_type", Object.Type),
        ("s_uvs_max", ctypes.c_int)
    ]