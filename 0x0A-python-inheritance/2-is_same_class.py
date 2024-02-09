#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """returns true if obj is an instance of a_class else false"""
    if type(obj) == a_class:
        return True
    elif type(obj) != a_class:
        return False
    
