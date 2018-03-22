#!/usr/bin/env python3
"""
Python package installation code. Does not include reference to the requirements file.

Created: 2018-03-22
Author: Donal Mee
"""
import inspect
import os
from setuptools import find_packages, setup
from typing import List


setup(
    name="travigy",
    version="1.0.0",
    url="https://github.com/ddmee/travis-git-python",

    author="Donal Mee",
    author_email="mee.donal@gmail.com",

    description="Demo of CI with python using Travis and Git",
    long_description=open("README.md").read(),

    packages=find_packages(),

    python_requires="==3.*",

    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
