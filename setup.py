#!/usr/bin/env python3
"""
Python package installation code

Created: 2018-03-22
Author: Donal Mee
"""
from setuptools import setup, find_packages


def readlines(fname):
    """ Read in file to array and strip out whitespace """
    with open(fname) as file:
        content = file.readlines()
        return [x.strip() for x in content]

setup(
    name="travigy",
    version="1.0.0",
    url="https://github.com/ddmee/travis-git-python",

    author="Donal Mee",
    author_email="mee.donal@gmail.com",

    description="Demo of CI with python using Travis and Git",
    long_description=open("README.md").read(),

    packages=find_packages(),

    install_requires=readlines("requirements.txt"),

    python_requires="==3.*",

    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
