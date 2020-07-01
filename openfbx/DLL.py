import ctypes

import platform

ofbx = None

if platform.system() == "Windows":
    ofbx = ctypes.WinDLL('./openfbx.dll')
else:
    ofbx = ctypes.CDLL('./openfbx.lib')
