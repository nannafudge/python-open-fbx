import ctypes
from ctypes import Structure


class RotationOrder(Structure):
    _fields_ = [
        ("EULER_XYZ", ctypes.c_int),
        ("EULER_XZY", ctypes.c_int),
        ("EULER_YZX", ctypes.c_int),
        ("EULER_YXZ", ctypes.c_int),
        ("EULER_ZXY", ctypes.c_int),
        ("EULER_ZYX", ctypes.c_int),
        ("SPHERIC_XYZ", ctypes.c_int)
    ]
