import ctypes


class Cursor(ctypes.Structure):
    _fields_ = [
        ("current", ctypes.POINTER(ctypes.c_uint8)),
        ("begin", ctypes.POINTER(ctypes.c_uint8)),
        ("end", ctypes.POINTER(ctypes.c_uint8))
    ]