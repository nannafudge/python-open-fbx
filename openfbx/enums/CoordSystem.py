import ctypes

class CoordSystem(ctypes.Structure):
    _fields = [
        ("CoordSystem_RightHanded", ctypes.c_int),
        ("CoordSystem_LeftHanded", ctypes.c_int)
    ]