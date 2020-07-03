import ctypes

from openfbx import DataView
from openfbx.structs.abstract.Texture import Texture


class TextureImpl(Texture):
    _fields_ = Texture._fields_ + [
        ("media", DataView),
        ("filename", DataView),
        ("relative_filename", DataView)
    ]
