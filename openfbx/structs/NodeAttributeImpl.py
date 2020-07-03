import ctypes

from openfbx.structs import DataView
from openfbx.structs.abstract.NodeAttribute import NodeAttribute


class NodeAttributeImpl(NodeAttribute):
    _fields_ = NodeAttribute._fields_ + [
        ("attribute_type", DataView)
    ]