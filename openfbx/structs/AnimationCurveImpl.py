import ctypes

from openfbx.structs.abstract.AnimationCurve import AnimationCurve


class AnimationCurveImpl(AnimationCurve):
    _fields_ = AnimationCurve._fields_ + [
        ("times", ctypes.c_int64 * 1),
        ("values", ctypes.c_float * 1)
    ]

    def get_key_count(self):
        return len(self.times)

    def get_key_time(self):
        return self.times.value[0]

    def get_key_value(self):
        return self.values.value[0]


