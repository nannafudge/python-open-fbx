import ctypes

from openfbx.structs.Object import Object, Matrix
from openfbx.structs.abstract.Skin import Skin


class Cluster(Object):
    _fields_ = Object._fields_ + [
        ("s_type", Object.Type)
    ]