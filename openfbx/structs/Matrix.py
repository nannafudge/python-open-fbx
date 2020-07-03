from _ctypes import Structure
import ctypes

class Matrix(Structure):
    _fields_ = [
        ("m", ctypes.c_double * 16)
    ]