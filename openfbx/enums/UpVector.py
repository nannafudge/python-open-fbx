import ctypes

class UpVector(ctypes.Structure):
    _fields = [
        ("UpVector_AxisX", ctypes.c_int),
        ("UpVector_AxisY", ctypes.c_int),
        ("UpVector_AxisZ", ctypes.c_int)
    ]