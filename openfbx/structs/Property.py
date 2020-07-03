import ctypes

from openfbx.structs.DataView import DataView
from openfbx.structs.interfaces.IElementProperty import IElementProperty


class Property(IElementProperty):
    _fields_ = IElementProperty._fields_ + [
        ("count", ctypes.c_int),
        ("type", ctypes.c_uint8),
        ("value", DataView),
        ("next", ctypes.POINTER(IElementProperty))
    ]
