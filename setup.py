import platform
import sys
import os

from glob import glob

from setuptools import setup, Extension


def build(target_platform):
    if target_platform == "windows":
        os_classifier = "Operating System :: Microsoft :: Windows :: Windows 10"
    if target_platform == "linux":
        os_classifier = "Operating System :: POSIX :: Linux"

    setup(
        platforms=target_platform,
        packages=[
            "openfbx",
            "openfbx.structs"
        ],
        data_files=[("openfbx", ["ofbx/openfbx.dll"])],
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'License :: OSI Approved :: MIT License',
            'Topic :: Artistic Software',
            'Topic :: Multimedia :: Graphics :: 3D Modeling',
            'Topic :: Software Development :: Libraries',
            os_classifier
        ],
    )


if __name__ == '__main__':
    # TODO: Build for linux too, add command line args
    build("windows")