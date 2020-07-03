import ctypes

from openfbx.structs import Object


class NodeAttribute(ctypes.Structure):
    _fields_ = [
        ("s_type", Object.Type)
    ]