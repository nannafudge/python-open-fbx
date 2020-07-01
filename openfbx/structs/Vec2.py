from _ctypes import Structure
import ctypes

class Vec2(Structure):
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double)
    ]