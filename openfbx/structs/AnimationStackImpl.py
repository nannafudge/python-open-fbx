import ctypes

from openfbx.structs.Object import Object
from openfbx.structs.abstract.AnimationStack import AnimationStack


class AnimationStackImpl(AnimationStack):
    _fields_ = AnimationStack._fields_ + [

    ]