import ctypes

from openfbx import DLL

class IElementProperty(ctypes.Structure):
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

