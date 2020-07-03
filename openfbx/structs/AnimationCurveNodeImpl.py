import ctypes
from ctypes import Structure

from openfbx.structs.Scene import Scene
from openfbx.structs.DataView import DataView
from openfbx.structs.Object import Object
from openfbx.structs.Element import Element
from openfbx.structs.abstract import AnimationCurveNode, AnimationCurve


class AnimationCurveNodeImpl(AnimationCurveNode):
    class Curve(ctypes.Structure):
        _fields_ = [
            ("curve", ctypes.POINTER(AnimationCurve)),
            ("connection", ctypes.POINTER(Scene.Connection))
        ]

    class Mode(ctypes.Structure):
        _fields_ = [
            ("TRANSLATION", ctypes.c_int),
            ("ROTATION", ctypes.c_int),
            ("SCALE", ctypes.c_int)
        ]

    _fields_ = AnimationCurveNode._fields_ + [
        ("default_values", ctypes.c_int * 3),
        ("dx", ctypes.POINTER(Element)),
        ("dy", ctypes.POINTER(Element)),
        ("dz", ctypes.POINTER(Element)),
        ("curves", Curve * 1),
        ("bone", ctypes.POINTER(Object)),
        ("bone_link_property", DataView),
        ("mode", Mode)
    ]