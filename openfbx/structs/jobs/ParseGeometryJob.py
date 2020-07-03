import ctypes

from openfbx.structs import Element, GeometryImpl


class ParseGeometryJob(ctypes.Structure):
    _fields_ = [
        ("element", ctypes.POINTER(Element)),
        ("triangulate", ctypes.c_bool),
        ("geom", GeometryImpl),
        ("id", ctypes.c_uint64),
        ("is_error", ctypes.c_bool)
    ]