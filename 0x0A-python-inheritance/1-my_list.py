#!/usr/bin/python3
"""Defines Mylist that inherits from list"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """prints the object's list in ascending sort"""
        print(sorted(self))
