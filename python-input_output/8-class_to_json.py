#!/usr/bin/python3
"""
Function that returns the dictionary description with simple data st
(list, dictionary, string, integer, boolean) for JSON serialization of an o.
"""

def class_to_json(obj):
    """
    Returns the dictionary representation of obj suitable for JSON serializat.

    Args:
        obj: instance of a class

    Returns:
        dict: dictionary of the instance's attributes
    """
    return obj.__dict__.copy()
