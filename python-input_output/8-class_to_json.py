#!/usr/bin/python3
"""
Function that returns the dictionary description with simple data structure
(list, dictionary, string, integer, boolean) for JSON serialization of an obje
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of obj suitable for JSON serializati.

    Args:
        obj: instance of a class

    Returns:
        dict: dictionary of the instance's attributes
    """
    return obj.__dict__.copy()
