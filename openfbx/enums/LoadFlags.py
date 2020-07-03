import ctypes

class LoadFlags(ctypes.Structure):
    _fields = [
        ("TRIANGULATE", ctypes.c_int),
        ("IGNORE_GEOMETRY", ctypes.c_int),
        ("IGNORE_BLEND_SHAPES", ctypes.c_int)
    ]