#!/usr/bin/python3
""" defining load_from_json_file function """

import json


def load_from_json_file(filename):
    """returns an object represented by a JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
