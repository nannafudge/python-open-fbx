from _ctypes import Structure
import ctypes

class Vec3(Structure):
    _fields_ = [
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float)
    ]