import ctypes
from ctypes import Structure


class LoadFlags(Structure):
    _fields_ = [
        ("TRIANGULATE", ctypes.c_int),
        ("IGNORE_GEOMETRY", ctypes.c_int),
        ("IGNORE_BLEND_SHAPES", ctypes.c_int)
    ]