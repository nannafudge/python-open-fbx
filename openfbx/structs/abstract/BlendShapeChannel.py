import ctypes

from openfbx.structs.Object import Object


class BlendShapeChannel(Object):
    _fields_ = Object._fields_ + [
        ("s_type", Object.Type)
    ]
