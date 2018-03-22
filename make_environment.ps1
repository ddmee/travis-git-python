#!/usr/bin/env powershell
# Author: Donal Mee
# This script will install the virtualenv, plus requirements, plus setup the pre-commit git hook
# Expect this script to only be used on Windows
if (${env:OS} -eq "Windows_NT") {
    "You are on windows"
}
else {
    "Do not use this script on a OS other than Windows! Try make_environment.sh"
    exit 1
}
"Installing virtualenv (requires virtualenv to be installed on your system python)"
virtualenv venv
"Activating the virtualenv"
venv/Scripts/activate
pip install -r requirements.txt
cp pre-commit .git/hooks
