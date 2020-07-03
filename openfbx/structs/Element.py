import ctypes
from ctypes import Structure

from openfbx.structs.DataView import DataView
from openfbx.structs.Property import Property

from openfbx.structs.interfaces.IElement import IElement


class Element(IElement):
    _fields_ = IElement._fields_ + [
        ("id", DataView),
        ("child", ctypes.POINTER(IElement)),
        ("sibling", ctypes.POINTER(IElement)),
        ("first_property", ctypes.POINTER(Property))
    ]