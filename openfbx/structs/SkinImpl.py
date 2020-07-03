import ctypes

from openfbx.structs.abstract.Cluster import Cluster
from openfbx.structs.abstract.Skin import Skin


class SkinImpl(Skin):
    _fields_ = Skin._fields_ + [
        ("clusters", ctypes.POINTER(Cluster))
    ]