from ctypes import Structure

from openfbx.structs.Object import Object


class AnimationCurveNode(Object):
    _fields_ = Object._fields_ + [
        ("s_type", Object.Type)
    ]

    def get_curve(self):
        pass

    def get_node_local_transform(self):
        pass

    def get_bone(self):
        pass
