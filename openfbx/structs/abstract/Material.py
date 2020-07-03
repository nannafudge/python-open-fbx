import ctypes

from openfbx.structs.Object import Object


class Material(Object):
    _fields_ = [
        ("s_type", Object.Type)
    ]