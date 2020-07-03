from _ctypes import Structure
import ctypes

class Color(Structure):
    _fields_ = [
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float)
    ]