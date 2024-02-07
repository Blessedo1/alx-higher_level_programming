#!/usr/bin/python3
"""Defines a file to be appended and returns number of characters added"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, mode='a', encoding='UTF8') as f:
        filename = f.write(text)
    return len(text)
