from ctypes import Structure

from openfbx.structs.Object import Object


class AnimationCurve(Object):
    _fields_ = Object._fields_ + [
        ("s_type", Object.Type)
    ]

    def get_key_count(self):
        pass

    def get_key_time(self):
        pass

    def get_key_value(self):
        pass