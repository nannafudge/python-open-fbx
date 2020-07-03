import ctypes

from openfbx.structs.Fbx import Fbx
from openfbx.structs.interfaces.IElement import IElement


class Object(Fbx):
    _fields_ = [
        ("id", ctypes.c_uint64),
        ("name", ctypes.c_char * 128),
        ("element", IElement),
        ("node_attribute", ctypes.POINTER(Fbx)),
        ("is_node", ctypes.c_bool),
        ("scene", Fbx)
    ]

    class Type(ctypes.Structure):
        _fields_ = [
            ("ROOT", ctypes.c_int),
            ("GEOMETRY", ctypes.c_int),
            ("SHAPE", ctypes.c_int),
            ("MATERIAL", ctypes.c_int),
            ("MESH", ctypes.c_int),
            ("TEXTURE", ctypes.c_int),
            ("LIMB_NODE", ctypes.c_int),
            ("NULL_NODE", ctypes.c_int),
            ("NODE_ATTRIBUTE", ctypes.c_int),
            ("CLUSTER", ctypes.c_int),
            ("SKIN", ctypes.c_int),
            ("BLEND_SHAPE", ctypes.c_int),
            ("BLEND_SHAPE_CHANNEL", ctypes.c_int),
            ("ANIMATION_STACK", ctypes.c_int),
            ("ANIMATION_LAYER", ctypes.c_int),
            ("ANIMATION_CURVE", ctypes.c_int),
            ("ANIMATION_CURVE_NODE", ctypes.c_int),
            ("POSE", ctypes.c_int)
        ]

    def getType(self):
        return None

    def getScene(self):
        pass

    def resolveObjectLink(self, idx):
        pass

    def resolveObjectLink(self, _type, property, idx):
        pass

    def resolveObjectLinkReverse(self, _type):
        pass

    def getParent(self):
        pass

    def getRotationOrder(self):
        pass

    def getRotationOffset(self):
        pass

    def getRotationPivot(self):
        pass

    def getPostRotation(self):
        pass

    def getScalingOffset(self):
        pass

    def getScalingPivot(self):
        pass

    def getPreRotation(self):
        pass

    def getLocalTranslation(self):
        pass

    def getLocalRotation(self):
        pass

    def getLocalScaling(self):
        pass

    def getGlobalTransform(self):
        pass

    def getLocalTransform(self):
        pass

    def evalLocal(self, translation, rotation):
        pass

    def evalLocal(self, translation, rotation, scaling):
        pass

    def isNode(self):
        return False

    def resolveObjectLink(self, idx):
        return None