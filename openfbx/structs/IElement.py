from ctypes import Structure

from openfbx import DLL

class IElement(Structure):
    def get_first_child(self):
        return DLL.ofbx.IElementGetFirstChild()
    def get_sibling(self):
        return DLL.ofbx.IElementGetSibling()
    def get_id(self):
        return DLL.ofbx.IElementGetID()
    def get_first_property(self):
        return DLL.ofbx.IElementGetFirstProperty()