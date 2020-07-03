import ctypes

from openfbx.structs import Color
from openfbx.structs.abstract import Texture
from openfbx.structs.abstract.Material import Material


class MaterialImpl(Material):
    _fields_ = Material._fields_ + [
        ("textures", ctypes.Array(Texture)),
        ("diffuse_color", Color),
        ("specular_color", Color),
        ("reflection_color", Color),
        ("ambient_color", Color),
        ("emissive_color", Color),

        ("diffuse_factor", ctypes.c_double),
        ("specular_factor", ctypes.c_double),
        ("reflection_factor", ctypes.c_double),
        ("shininess", ctypes.c_double),
        ("shininess_exponent", ctypes.c_double),
        ("ambient_factor", ctypes.c_double),
        ("bump_factor", ctypes.c_double),
        ("emissive_factor", ctypes.c_double)
    ]