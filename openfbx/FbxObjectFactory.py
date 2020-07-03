import ctypes

from openfbx import DLL
from openfbx.structs import AnimationCurveImpl


class FbxObjectFactory:
    # Objects in OpenFBX mostly all use this constructor format, please add additional methods for other classes that don't
    def create_object(self, objectName, args):
        # Array of arrays to existing objects
        if type(args, [[]]) or not type(args, []):
            return DLL.ofbx.__getitem__(objectName + "Constructor1")(ctypes.byref(args))

        # Default Constructor
        if len(args) == 0 or args is None:
            return DLL.ofbx.__getitem__(objectName + "Constructor4")()

        # Scene and Element constructor
        if len(args) > 0:
            return DLL.ofbx.__getitem__(objectName + "Constructor3")(ctypes.byref(args[0]), ctypes.byref(args[1]))

        # Array to existing objects
        return DLL.ofbx.__getitem__(objectName + "Constructor2")(ctypes.byref(args))