import ctypes

from openfbx.structs.abstract.Geometry import Geometry
from openfbx.structs.abstract.Material import Material
from openfbx.structs.abstract.Mesh import Mesh
from openfbx.structs.abstract.Pose import Pose


class MeshImpl(Mesh):
    _fields_ = Mesh._fields_ + [
        ("pose", ctypes.POINTER(Pose)),
        ("geometry", ctypes.POINTER(Geometry)),
        ("materials", ctypes.POINTER(ctypes.POINTER(Material)))
    ]