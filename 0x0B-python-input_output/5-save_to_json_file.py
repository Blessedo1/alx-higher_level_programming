#!/usr/bin/python3
"""Function that writes an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """writes object to filename using JSON representation"""
    with open(filename, mode='w', encoding='UTF8') as f:
        filename = f.write(json.dumps(my_obj))
