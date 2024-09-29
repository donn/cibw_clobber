#!/usr/bin/env python3
import os
import shutil
import subprocess
from setuptools import setup, Extension

module_name = "example"
version = "0.1.0"

ext = Extension(
    name="_helloworld",
    sources=[
        "src/hello.c",
    ],
    include_dirs=[
        "libparse",
    ],
)

subprocess.check_call(["python3", "--version"])
subprocess.check_call(
    [
        f"{os.path.dirname(shutil.which("python3"))}/python3-config",
        "--includes",
    ]
)

setup(
    name=module_name,
    packages=["example"],
    version=version,
    description="example package to demonstrate clobbering behavior in cibuildwheel",
    install_requires=["wheel"],
    python_requires=">3.8",
    ext_modules=[ext],
)
