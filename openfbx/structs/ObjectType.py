import ctypes


class ObjectType(ctypes.Structure):
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

