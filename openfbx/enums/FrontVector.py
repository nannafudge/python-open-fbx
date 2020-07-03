import ctypes

class FrontVector(ctypes.Structure):
    _fields = [
        ("FrontVector_ParityEven", ctypes.c_int),
        ("FrontVector_ParityOdd", ctypes.c_int)    ]