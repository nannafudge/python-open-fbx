import ctypes

class DataView(ctypes.Structure):
    _fields_ = [
        ("begin", ctypes.POINTER(ctypes.c_uint8)),
        ("end", ctypes.POINTER(ctypes.c_uint8)),
        ("isBinary", ctypes.c_bool)
    ]