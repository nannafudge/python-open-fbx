import ctypes

from openfbx.structs.Object import Object


class Texture(Object):
    class TextureType(ctypes.Structure):
        _fields_ = [
            ("DIFFUSE", ctypes.c_int),
            ("NORMAL", ctypes.c_int),
            ("SPECULAR", ctypes.c_int),
            ("SHININESS", ctypes.c_int),
            ("AMBIENT", ctypes.c_int),
            ("EMISSIVE", ctypes.c_int),
            ("REFLECTION", ctypes.c_int),
            ("COUNT", ctypes.c_int)
        ]

    _fields_ = Object._fields_ + [
        ("s_type", Object.Type)
    ]