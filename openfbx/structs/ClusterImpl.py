import ctypes

from openfbx.structs.Object import Object, Matrix
from openfbx.structs.abstract.Cluster import Cluster
from openfbx.structs.abstract.Skin import Skin


class ClusterImpl(Cluster):
    _fields_ = Cluster._fields_ + [
        ("link", ctypes.POINTER(Object)),
        ("skin", ctypes.POINTER(Skin)),
        ("indices", ctypes.Array(ctypes.c_int)),
        ("weights", ctypes.Array(ctypes.c_double)),
        ("transform_matrix", Matrix),
        ("transform_link_matrix", Matrix)
    ]
