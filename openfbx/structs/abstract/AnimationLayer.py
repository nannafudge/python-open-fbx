from openfbx.structs.Object import Object


class AnimationLayer(Object):
    _fields = Object._fields_ + [
        ("s_type", Object.Type)
    ]
