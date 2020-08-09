"""Inital Conftest
This will allow for the contest root to be passed to the tests
https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files
"""
import os
import sys


PKG_ROOT = os.path.normcase(os.path.abspath(os.path.join(os.path.dirname(__file__), "source")))
if PKG_ROOT not in sys.path:
    sys.path.append(PKG_ROOT)
