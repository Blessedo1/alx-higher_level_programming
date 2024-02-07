#!/usr/bin/python3
"""Defines a text file character-counting function"""


def write_file(filename="", text=""):
    """Writes a string to the textfile and returns number of characters."""
    with open(filename, mode="w", encoding="utf-8") as f:
        filename = f.write(text)
    return len(text)
