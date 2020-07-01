import ctypes
from ctypes import Structure

from openfbx.structs.Page import Page
from openfbx.structs.Vec3 import Vec3


class Allocator(Structure):
    _fields_ = [
        ("first", ctypes.pointer(Page)),
        ("tmp", ctypes.c_float),
        ("int_tmp", ctypes.c_int),
        ("vec3_tmp", Vec3),
        ("double_tmp", ctypes.c_double),
        ("vec3_tmp2", Vec3)
    ]

    def allocate(self, **kwargs):
        pass

    class Page(Structure):
        _fields_ = [
            ("data", ctypes.Array(ctypes.c_uint8))
        ]

        class Header(Structure):
            _fields_ = [
                ("next", ctypes.pointer(Page)),
                ("offset", ctypes.c_uint32)
            ]