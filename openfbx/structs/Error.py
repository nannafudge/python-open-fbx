import ctypes


class Error(ctypes.Structure):
    _fields_ = [
        ("s_message", ctypes.POINTER(ctypes.c_char))
    ]