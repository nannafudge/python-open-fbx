from _ctypes import Structure
import ctypes

class Vec4(Structure):
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double),
        ("z", ctypes.c_double),
        ("w", ctypes.c_double)
    ]