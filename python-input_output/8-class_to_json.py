#!/usr/bin/python3
"""
Function that returns the dictionary description with simple data structure
(list, dictionary, string, integer, boolean) for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary representation of obj suitable for JSON serialization.

    Args:
        obj: instance of a class

    Returns:
        dict: dictionary of the instance's attributes
    """
    return obj.__dict__.copy()
