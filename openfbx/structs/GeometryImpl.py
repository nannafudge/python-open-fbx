import ctypes

from openfbx import Vec3, Vec2, Vec4
from openfbx.structs.abstract.BlendShape import BlendShape
from openfbx.structs.abstract.Geometry import Geometry
from openfbx.structs.abstract.Skin import Skin


class GeometryImpl(Geometry):
    class VertexDataMapping(ctypes.Structure):
        _fields_ = [
            ("BY_POLYGON_VERTEX", ctypes.c_int),
            ("BY_POLYGON", ctypes.c_int),
            ("BY_VERTEX", ctypes.c_int)
        ]

    class NewVertex(ctypes.Structure):
        _fields = [
            ("index", ctypes.c_int),
            ("next", ctypes.POINTER(NewVertex))
        ]

    _fields_ = Geometry._fields_ + [
        ("vertices", ctypes.Array(Vec3)),
        ("normals", ctypes.Array(Vec3)),
        ("uvs", ctypes.Array(Vec2)),
        ("colors", ctypes.Array(Vec4)),
        ("tangents", ctypes.Array(Vec3)),
        ("materials", ctypes.Array(ctypes.c_int)),

        ("skin", ctypes.POINTER(Skin)),
        ("blendShape", ctypes.POINTER(BlendShape)),

        ("indices", ctypes.Array(ctypes.c_int64)),
        ("to_old_vertices", ctypes.Array(ctypes.c_int64)),
        ("to_new_vertices", ctypes.Array(NewVertex))
    ]