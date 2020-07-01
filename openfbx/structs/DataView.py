from _ctypes import Structure
import ctypes

from openfbx import DLL

DLL.ofbx.DataViewToU64.restype = ctypes.c_ulonglong
DLL.ofbx.DataViewToI64.restype = ctypes.c_ulonglong
DLL.ofbx.DataViewToInt.restype = ctypes.c_ulonglong
DLL.ofbx.DataViewToU32.restype = ctypes.c_ulonglong
DLL.ofbx.DataViewToDouble.restype = ctypes.c_ulonglong
DLL.ofbx.DataViewToFloat.restype = ctypes.c_ulonglong

class DataView(Structure):
    _fields_ = [
        ("begin", ctypes.pointer(ctypes.c_uint8())),
        ("end", ctypes.pointer(ctypes.c_uint8())),
        ("isBinary", ctypes.c_bool)
    ]

    def to_u64(self):
        return DLL.ofbx.DataViewToU64()
    def to_i64(self):
        return DLL.ofbx.DataViewToI64()
    def to_int(self):
        return DLL.ofbx.DataViewToInt()
    def to_u32(self):
        return DLL.ofbx.DataViewToU32()
    def to_double(self):
        return DLL.ofbx.DataViewToDouble()
    def to_float(self):
        return DLL.ofbx.DataViewToFloat()

    def toString(self):
        return ""