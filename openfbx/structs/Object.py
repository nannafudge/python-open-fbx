import ctypes

from openfbx import DLL, Scene
from openfbx.structs.IElement import IElement
from openfbx.structs.ObjectType import ObjectType

class Object(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_uint64),
        ("name", ctypes.Array(ctypes.c_char)),
        ("element", ctypes.py_object(IElement)),
        ("node_attribute", ctypes.pointer(ctypes.py_object())),

        ("is_node", ctypes.c_bool),
        ("scene", ctypes.byref(ctypes.py_object(Scene)))
    ]

    def getType(self):
        return ctypes.py_object(ObjectType)

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
        DLL.ofbx.__getitem__("resolveObjectLink")
