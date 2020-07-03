import ctypes
import unittest

import openfbx
from openfbx import DLL
from openfbx.structs.MeshImpl import MeshImpl


class TestMainFunctions(unittest.TestCase):
    def test_load(self):
        scene = openfbx.load("objects/handgun.fbx")
        res = scene.m_meshes[0].contents

        print(res.getType())