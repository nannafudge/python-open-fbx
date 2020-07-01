# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound
import platform

from openfbx.structs.Allocator import Allocator
from openfbx.structs.Color import Vec3
from openfbx.structs.Element import Element
from openfbx.structs.IScene import IScene
from openfbx.structs.Matrix import Matrix
from openfbx.structs.Object import Object
from openfbx.structs.ObjectType import ObjectType
from openfbx.structs.Scene import Scene
from openfbx.structs.Type import Type

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound

from openfbx.structs import *

import ctypes

if platform.system() == "Windows":
    lib = ctypes.WinDLL('openfbx.dll')

if platform.system() == "Linux":
    lib = ctypes.CDLL('openfbx.lib')

# Functions

# Object.struct
lib.ObjectGetParent.argtypes = []
lib.ObjectGetParent.restype = ctypes.pointer(Object)
lib.ObjectResolveObjectLinkInt.argtypes = [ctypes.c_int]
lib.ObjectResolveObjectLinkInt.restype = ctypes.pointer(Object)
lib.ObjectResolveObjectLinkType.argtypes = [Type, ctypes.c_char_p, ctypes.c_int]
lib.ObjectResolveObjectLinkType.restype = ctypes.pointer(Object)
lib.ObjectResolveObjectLinkReverse.argtypes = [Type]
lib.ObjectResolveObjectLinkReverse.restype = ctypes.pointer(Object)
lib.ObjectGetScene.argtypes = []
lib.ObjectGetScene.restype = IScene
lib.ObjectGetLocalTransform.argtypes = []
lib.ObjectGetLocalTransform.restype = Matrix
lib.ObjectGetGlobalTransform.argtypes = []
lib.ObjectGetGlobalTransform.restype = Matrix
lib.ObjectGetLocalScaling.argtypes = []
lib.ObjectGetLocalScaling.restype = Vec3
lib.ObjectGetLocalRotation.argtypes = []
lib.ObjectGetLocalRotation.restype = Vec3
lib.ObjectGetPreRotation.argtypes = []
lib.ObjectGetPreRotation.restype = Vec3
lib.ObjectGetLocalTranslation.argtypes = []
lib.ObjectGetLocalTranslation.restype = Vec3
lib.ObjectEvalLocal1.argtypes = []
lib.ObjectEvalLocal1.restype = Matrix
lib.ObjectEvalLocal2.argtypes = []
lib.ObjectEvalLocal2.restype = Matrix
lib.ObjectIsNode.argtypes = []
lib.ObjectIsNode.restype = ctypes.c_bool

lib.ObjectGetScalingPivot.argtypes = []
lib.ObjectGetScalingPivot.restype = Vec3
lib.ObjectGetScalingOffset.argtypes = []
lib.ObjectGetScalingOffset.restype = Vec3
lib.ObjectGetPostRotation.argtypes = []
lib.ObjectGetPostRotation.restype = Vec3
lib.ObjectGetRotationPivot.argtypes = []
lib.ObjectGetRotationPivot.restype = Vec3
lib.ObjectGetRotationOffset.argtypes = []
lib.ObjectGetRotationOffset.restype = Vec3
lib.ObjectGetRotationOrder.argtypes = []
lib.ObjectGetRotationOrder.restype = ObjectType

PostprocessBlendShapeChannel
PostprocessCluter
PostprocessPose
PostprocessShape

lib.FromString.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.py_object]
lib.FromString.restype = ctypes.c_char_p
lib.ParseVideo.argtypes = [ctypes.byref(Scene), ctypes.byref(Element), ctypes.byref(Allocator)]
lib.ParseVideo.restype = None
lib.GetEmebeddedData.argtypes = []
lib.GetEmebeddedData.restype = ctypes.

lib.IElementPropertyGetCount.restype = ctypes.c_int

lib.fbx_time_to_seconds.rettypes = ctypes.c_double
lib.fbx_time_to_seconds.argtypes = ctypes.c_int
lib.from_string.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]

lib.load.rettypes = Vector2
lib.load.argtypes = [ctypes.POINTER(ctypes.c_int8), ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]


def load(data, size, flags, job_proocessor, job_user_ptr):
    lib.load(data, size, flags, job_proocessor, job_user_ptr)


def fbx_time_to_seconds(time):
    lib.fbx_time_to_seconds(ctypes.c_int(time))


def from_string_int(str, end, val):
    if val is int:
        lib.from_string.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
        lib.from_string(str, end, val)