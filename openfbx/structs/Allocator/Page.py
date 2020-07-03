import ctypes

from openfbx.structs.Allocator.Header import Header
from openfbx.structs.Allocator.IPage import IPage


class Page(IPage):
    _fields_ = IPage._fields_ + [
        ("header", Header),
        ("data", ctypes.c_uint8 * (4096 * 1024 - 12))
    ]