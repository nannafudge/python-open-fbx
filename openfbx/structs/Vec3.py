from _ctypes import Structure
import ctypes

class Vec3(Structure):
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double),
        ("z", ctypes.c_double)
    ]