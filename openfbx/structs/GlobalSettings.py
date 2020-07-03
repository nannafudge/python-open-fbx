import ctypes

class GlobalSettings(ctypes.Structure):
    _fields_ = [
        ("UpAxis", ctypes.c_int),
        ("UpAxisSign", ctypes.c_int),
        ("FrontAxis", ctypes.c_int),
        ("FrontAxisSign", ctypes.c_int),
        ("CoordAxis", ctypes.c_int),
        ("CoordAxisSign", ctypes.c_int),
        ("OriginalUpAxis", ctypes.c_int),
        ("OriginalUpAxisSign", ctypes.c_int),
        ("UnitScaleFactor", ctypes.c_int),
        ("OriginalUnitScaleFactor", ctypes.c_int),
        ("TimeSpanStart", ctypes.c_double),
        ("TimeSpanStop", ctypes.c_double),
        ("TimeMode", ctypes.c_int),
        ("CustomFrameRate", ctypes.c_int),
    ]