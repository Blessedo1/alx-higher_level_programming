#!/usr/bin/python3
"""Decodes from a JSON data to a python representation"""


import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    return json.loads(my_str)
