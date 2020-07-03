import ctypes

from openfbx.structs.Object import Object
from openfbx.structs.abstract.BlendShape import BlendShape
from openfbx.structs.abstract.BlendShapeChannel import BlendShapeChannel


class BlendShapeImpl(BlendShape):
    _fields_ = BlendShape._fields_ + [
        ("blendShapeChannels", ctypes.Array(ctypes.POINTER(BlendShapeChannel)))
    ]