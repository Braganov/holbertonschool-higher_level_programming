#!/usr/bin/env python3

"""
Module for basic serialization and deserialization
of a Python dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The filename of the JSON file.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it back into a Python dictionary.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
