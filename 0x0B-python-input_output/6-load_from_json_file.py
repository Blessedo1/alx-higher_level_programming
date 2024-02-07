#!/usr/bin/python3
"""Object creation"""


import json


def load_from_json_file(filename):
    """function that creates an object from a JSON file"""
    with open(filename) as f:
        json.load(f)
