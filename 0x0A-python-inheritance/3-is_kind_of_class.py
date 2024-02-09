#!/usr/bin/python3
"""Function checks if an object is an instance of a subclass or baseclass"""


def is_kind_of_class(obj, a_class):
    """returns true if obj is an instance of a_class"""
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
