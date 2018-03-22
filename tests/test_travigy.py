#!/usr/bin/env python3
"""
Unit tests with pytest for travigy app.

Created: 2018-03-22
Author: Donal Mee
"""
from io import StringIO
import sys
import pytest
from travigy.__main__ import main

def test_main():
    captured_output = StringIO()
    sys.stdout = captured_output
    main()
    assert "hello ci world" in captured_output.getvalue()
