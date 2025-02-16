#!/usr/bin/env python3
"""
Module for serializing and deserializing a dictionary to/from XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The XML file to save the serialized data.

    Returns:
        bool: True if successful, False otherwise.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
