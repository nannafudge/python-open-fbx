import ctypes

from openfbx.structs.abstract.BlendShape import BlendShape
from openfbx.structs.abstract.BlendShapeChannel import BlendShapeChannel
from openfbx.structs.abstract.Shape import Shape


class BlendShapeChannelImpl(BlendShapeChannel):
    _fields_ = BlendShape._fields_ + [
        ("blendShape", ctypes.POINTER(BlendShape)),
        ("deformPercent", ctypes.c_double),
        ("fullWeights", ctypes.Array(ctypes.c_double)),
        ("shapes", ctypes.Array(Shape))
    ]
