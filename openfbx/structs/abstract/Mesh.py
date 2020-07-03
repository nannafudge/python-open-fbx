import ctypes

from openfbx.structs.Object import Object


class Mesh(Object):
    _fields_ = [
        ("s_type", Object.Type)
    ]