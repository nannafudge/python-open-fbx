import ctypes

from openfbx.structs import AnimationCurveNodeImpl
from openfbx.structs.abstract.AnimationLayer import AnimationLayer


class AnimationLayerImpl(AnimationLayer):
    _fields_ = AnimationLayer._fields_ + [
        ("curve_nodes", ctypes.Array(ctypes.POINTER(AnimationCurveNodeImpl)))
    ]
