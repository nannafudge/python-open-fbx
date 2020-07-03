import ctypes

from openfbx import Vec3
from openfbx.structs.abstract.Shape import Shape


class ShapeImpl(Shape):
    _fields_ = Shape._fields_ + [
        ("vertices", ctypes.Array(Vec3)),
        ("normals", ctypes.Array(Vec3))
    ]