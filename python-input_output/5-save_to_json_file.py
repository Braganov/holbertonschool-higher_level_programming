#!/usr/bin/python3
"""difining save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using a JSON representation"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
