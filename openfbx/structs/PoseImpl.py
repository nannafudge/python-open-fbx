import ctypes

from openfbx.structs.Object import Object, DataView, Matrix
from openfbx.structs.abstract.Pose import Pose


class PoseImpl(Pose):
    _fields_ = Pose._fields_ + [
        ("matrix", Matrix),
        ("node", ctypes.POINTER(Object)),
        ("node_id", DataView)
    ]