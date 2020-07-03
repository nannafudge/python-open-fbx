# -*- coding: utf-8 -*-
import _ctypes
import ctypes
import logging
from itertools import count
from typing import Any, overload, Iterable, List

from pkg_resources import get_distribution, DistributionNotFound

from openfbx import DLL
from openfbx.structs.OptionalError import OptionalError
from openfbx.structs.Allocator import Allocator
from openfbx.structs.Color import Color
from openfbx.structs.Element import Element
from openfbx.structs.interfaces.IScene import IScene
from openfbx.structs.Matrix import Matrix
from openfbx.structs.Object import Object
from openfbx.structs.Scene import Scene
from openfbx.structs.Type import Type

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound

from openfbx.structs import *

DLL.ofbx.Load.restype = ctypes.POINTER(Scene)

DLL.ofbx.FbxTimeToSeconds.restype = ctypes.c_double
DLL.ofbx.FbxTimeToSeconds.argtypes = [ctypes.c_int64]

DLL.ofbx.SecondsToFbxTime.restype = ctypes.c_int64
DLL.ofbx.SecondsToFbxTime.argtypes = [ctypes.c_double]

DLL.ofbx.ParseVideo.restype = None
DLL.ofbx.ParseVideo.argtypes = [Scene, Element, Allocator]

DLL.ofbx.ParseTexture.restype = ctypes.Structure
DLL.ofbx.ParseTexture.argtypes = [Scene, Element, Allocator]

DLL.ofbx.ParsePose.restype = ctypes.Structure
DLL.ofbx.ParsePose.argtypes = [Scene, Element, Allocator]

DLL.ofbx.sync_job_processor.restype = None
DLL.ofbx.sync_job_processor.argTypes = [ctypes.CFUNCTYPE, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32]

class _Array(ctypes.Array):
    arr = []

    _type_ = ctypes.c_int * 1
    _length_ = arr.__len__()

    def __init__(self, *args: Any) -> None:
        arr = args

    @overload
    def __getitem__(self, i: int) -> Any:
        return self.arr.__getitem__(i)

    @overload
    def __getitem__(self, s: slice) -> List[Any]:
        items = []
        s.stop = max(s.stop, len(self.arr))

        for i in range(s.start, s.stop, s.step):
            items.append(self.arr.__getitem__(i))

        return items

    def __getitem__(self, i: int) -> Any:
        return self.arr.__getitem__(i)

    @overload
    def __setitem__(self, s: slice, o: Iterable[Any]) -> None:
        s.stop = max(s.stop, len(self.arr))

        for obj in o:
            for i in range(s.start, s.stop, s.step):
                self.arr.__setitem__(i, obj)

    def __setitem__(self, i: int, o: Any) -> None:
        self.arr.__setitem__(i, o)


def load(filepath):
    with (open(filepath, 'rb')) as buffer:
        fbx = buffer.read()

        buffer = (ctypes.c_uint8 * len(fbx))()

        for i, byte in enumerate(fbx):
            buffer[i] = int(byte)

        DLL.ofbx.Load.argtypes = [ctypes.POINTER(ctypes.c_uint8 * len(fbx)), ctypes.c_int, ctypes.c_uint64]
        return DLL.ofbx.Load(ctypes.pointer(buffer), len(fbx), ctypes.c_uint64(0), None, None).contents


def load_raw(data, size, flags, job_processor, job_user_ptr):
    return DLL.ofbx.Load(data, size, flags, job_processor, job_user_ptr).contents

def fbx_time_to_seconds(time):
    return DLL.ofbx.FbxTimeToSeconds(ctypes.c_int(time)).value

def seconds_to_fbx_time(time):
    return DLL.ofbx.SecondsToFbxTime(ctypes.c_double(time)).value

def parse_video(scene, element, allocator):
    DLL.ofbx.ParseVideo(ctypes.byref(scene), ctypes.byref(element), ctypes.byref(allocator))

def parse_texture(scene, element, allocator):
    DLL.ofbx.ParseTexture(ctypes.byref(scene), ctypes.byref(element), ctypes.byref(allocator))

def parse_pose(scene, element, allocator):
    DLL.ofbx.ParsePose(ctypes.byref(scene), ctypes.byref(element), ctypes.byref(allocator))

def sync_job_processor(job_function, func, data, size, count):
    DLL.ofbx.sync_job_processor(job_function, ctypes.c_void_p(func), ctypes.c_void_p(data), ctypes.c_uint32(size), ctypes.c_uint32(count))