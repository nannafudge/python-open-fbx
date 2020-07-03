import ctypes

from openfbx.structs.Allocator.IPage import IPage


class Header(ctypes.Structure):
    _fields_ = [
        ("next", ctypes.POINTER(IPage)),
        ("offset", ctypes.c_uint32)
    ]