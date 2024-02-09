#!/usr/bin/python3
"""Function checks an object being an instance of subclass of specified class"""


def inherits_from(obj, a_class):
    """return True if an object is an instance of a subclass else False"""
    if issubclass(type(obj), a_class) is True:
        if type(obj) is not a_class:
            return True
    else:
        return False
