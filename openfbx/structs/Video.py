import ctypes

from openfbx.structs.DataView import DataView


class Video(ctypes.Structure):
    _fields_ = [
        ("filename", DataView),
        ("content", DataView),
        ("media", DataView)
    ]