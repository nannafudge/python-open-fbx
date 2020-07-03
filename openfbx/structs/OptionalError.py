import ctypes

from openfbx.structs.Object import Object
from openfbx.structs.Error import Error


class OptionalError(Error):
    _fields_ = Error._fields_ + [
        ("value", ctypes.POINTER(Object)),
        ("is_error", ctypes.c_bool)
    ]
