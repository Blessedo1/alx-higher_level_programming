#!/usr/bin/python3
"""Checks an object being an instance of subclass of specified class"""


def inherits_from(obj, a_class):
    """return True if an object is an instance of a subclass else False"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
