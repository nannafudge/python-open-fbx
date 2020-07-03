import ctypes

from openfbx.structs.DataView import DataView


class TakeInfo(ctypes.Structure):
    _fields_ = [
        ("name", DataView),
        ("filename", DataView),
        ("local_time_from", ctypes.c_double),
        ("local_time_to", ctypes.c_double),
        ("reference_time_from", ctypes.c_double),
        ("reference_time_to", ctypes.c_double)
    ]