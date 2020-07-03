import ctypes

class FrameRate(ctypes.Structure):
    _fields = [
        ("FrameRate_DEFAULT", ctypes.c_int),
        ("FrameRate_120", ctypes.c_int),
        ("FrameRate_100", ctypes.c_int),
        ("FrameRate_60", ctypes.c_int),
        ("FrameRate_50", ctypes.c_int),
        ("FrameRate_48", ctypes.c_int),
        ("FrameRate_30", ctypes.c_int),
        ("FrameRate_30_DROP", ctypes.c_int),
        ("FrameRate_NTSC_DROP_FRAME", ctypes.c_int),
        ("FrameRate_NTSC_FULL_FRAME", ctypes.c_int),
        ("FrameRate_PAL", ctypes.c_int),
        ("FrameRate_CINEMA", ctypes.c_int),
        ("FrameRate_1000", ctypes.c_int),
        ("FrameRate_CINEMA_ND", ctypes.c_int),
        ("FrameRate_CUSTOM", ctypes.c_int)
    ]