import ctypes
from ctypes import Structure

from openfbx import DLL

class IElementProperty(Structure):
    class Type(Structure):
        _fields_ = [
            ("LONG", ctypes.c_char),
            ("INTEGER", ctypes.c_char),
            ("STRING", ctypes.c_char),
            ("FLOAT", ctypes.c_char),
            ("DOUBLE", ctypes.c_char),
            ("ARRAY_DOUBLE", ctypes.c_char),
            ("ARRAY_INT", ctypes.c_char),
            ("ARRAY_LONG", ctypes.c_char),
            ("ARRAY_FLOAT", ctypes.c_char),
            ("BINARY",ctypes.c_char)
        ]

    def getType(self):
        pass

    def getNext(self):
        return DLL.ofbx.IElementPropertyGetNext()

    def getValue(self):
        pass

    def getCount(self):
        pass

    def getValues(values, max_size):
        pass

    # getValues(int* values, int max_size)
    # getValues(float* values, int max_size)
    # getValues(u64* values, int max_size)
    # getValues(i64* values, int max_size)

    _fields_ = [

    ]

