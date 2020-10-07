import os
import pathlib
import re
import subprocess
import sys

from setuptools import Command, find_packages, setup
from setuptools.extension import Extension

# Check Python version, no point installing if unsupported version inplace
min_version = (3, 6)
if sys.version_info < min_version:
    py_version = ".".join([str(n) for n in sys.version_info])
    msg = (
        f"Python-{'.'.join(min_version)} or greater is required, "
        f"Python-{py_version} used."
    )
    raise RuntimeError(msg)


if "DONT_USE_CYTHON" in os.environ:
    raise ImportError
from Cython.Compiler.Version import version

version = tuple([int(v) for v in re.split("[^\d]", version) if v.isdigit()])
if version < (0, 17, 1):
    print("Your Cython version is too old")
    raise ImportError
from Cython.Build import cythonize

source_suffix = ".pyx"
PACKAGE_DIR = "src"


def CythonExtension(module_name, **kw):
    path = [PACKAGE_DIR] + module_name.split(".")
    path = os.path.join(*path) + source_suffix
    return Extension(module_name, [path], **kw)


setup(
    name="Graph Mode",
    version="0.0",
    description="An app that defines graphs.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["Cython"],
    extras_require={"dev": []},
    ext_modules=cythonize([CythonExtension("gm.hello_world"),]),
)
