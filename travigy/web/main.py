#!/usr/bin/env python3
"""
Bottle web server main module.

Created: 2018-03-24
Author: Donal Mee
"""
from bottle import route, run, template

@route("/")
def index():
    import pdb; pdb.set_trace()

def start():
    run(host="localhost", port=8080)
