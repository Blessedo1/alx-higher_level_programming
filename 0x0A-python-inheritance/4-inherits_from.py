#!/usr/bin/python3
"""Function checks an object being an instance of subclass of specified class"""


def inherits_from(obj, a_class):
    """return True if it isn't an instance else return false"""
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
