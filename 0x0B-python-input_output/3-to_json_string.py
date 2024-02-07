#!/usr/bin/python3
import json
"""Returns the JSON representation of an object"""


def to_json_string(my_obj):
    """Encodes python object string in JSON"""
    return json.dumps(my_obj)
