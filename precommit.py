#!/usr/bin/env python
"""
Git precommit python hook. Run tests before a commit.

Created: 2018-03-22
Author: Donal Mee

HOW DOES THIS WORK?
- Activates the virtualenv, by importing the activation module.
- Runs unit tests with pytest. If any unit test fails, the script exist with non-zero number.

BY DEFAULT THIS SCRIPT IS NOT ENABLED.
To add this script before each commit, invoke this script in the ./git/hooks/precommit file.
But, if you run the make_environment scripts, it will be installed for you.

Setup:
- Open pre-commit in the root of this project. Check that the VENV_DIR variable is suitable
for your local system. Edit and save it.
- Then copy pre-commit file to /.git/hooks/

This will cause git to run THIS script (i.e. precommit.py) before every commit.
"""
# standard
import importlib.util
import os
import platform
import sys
import time
# third party
import pytest


def activate_virtualenv(venv_dir: str) -> None:
    """Activates the virtualenv. Operating system sensitive. Supports Windows/OSx/Linux.

    :param venv_dir: path to the virtualenv directory.

    Is there not an easy way to activate a virtualenv? I have found that the built-in python
    activation script is not reliable. Therefore, I am have had to help it a little.

    Raises FileNotFoundError or RuntimeError if cannot activate the virtualenv.
    """
    # Need to check whether on windows or other, because directory of activation script differs.
    operating_system = platform.system().lower()
    if operating_system == "windows":
        venv_scripts = "Scripts"
    elif operating_system in ["linux", "darwin"]:
        venv_scripts = "bin"
    else:
        raise RuntimeError("Unrecognised operating system: {}".format(operating_system))

    # Get the path to the activation script, which we will execute by importing
    venv_file = os.path.join(str(venv_dir), venv_scripts, "activate_this.py")
    spec = importlib.util.spec_from_file_location("activate_this", venv_file)
    activate_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(activate_mod)

    # check if virtualenv has been activated
    # https://stackoverflow.com/questions/1871549/python-determine-if-running-inside-virtualenv#1883251
    if hasattr(sys, "real_prefix"):
        print("virtualenv activated.")
    else:
        raise RuntimeError("Unable to activate expected virtualenv: {}.".format(venv_file))

    return None


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("Please supply the virtualenv directory as the first argument to"
                         " precommit.py in the .git/hooks/pre-commit file.")
    else:
        if activate_virtualenv(sys.argv[1]):
            # pytest returns 0 if no unit tests pass, else returns another number.
            # pytest will print out the status of each test case.
            # But it will not print the traceback for a failure.
            sys.exit(pytest.main(['-v', '--tb', 'no', 'travigy/']))
        else: # could not activate virtualenv
            sys.exit(1)
