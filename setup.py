#!/usr/bin/env python

from __future__ import annotations

from setuptools import setup

setup(
    name="dask",
    readme="README.rst",
    install_requires=[
        # NOTE: These are tested in `continuous_integration/test_imports.sh` If
        # you modify these, make sure to change the corresponding line there.
        "click >= 8.1",
        "cloudpickle >= 1.5.0",
        "fsspec >= 2021.09.0",
        "packaging >= 20.0",
        "partd >= 1.2.0",
        "pyyaml >= 5.3.1",
        "toolz >= 0.10.0",
        # importlib.metadata has the following bugs fixed in 3.10.9 and 3.11.1
        # https://github.com/python/cpython/issues/99130
        # https://github.com/python/cpython/issues/98706
        # TODO: when Python 3.12 is support is added this could be a
        # conditional dependency
        "importlib_metadata >= 4.13.0",
    ],
    version="2023.0.1",
)
