import ctypes
from ctypes import Structure

from openfbx.structs.Vec3 import Vec3

from openfbx.structs.Allocator.Page import Page

from openfbx import DLL

class Allocator(Structure):
    _fields_ = [
        ("first", ctypes.POINTER(Page)),
        ("tmp", ctypes.c_float),
        ("int_tmp", ctypes.c_int),
        ("vec3_tmp", Vec3),
        ("double_tmp", ctypes.c_double),
        ("vec3_tmp2", Vec3)
    ]

    def allocate(self, **kwargs):
        return DLL.ofbx.AllocatorAllocate(kwargs).value