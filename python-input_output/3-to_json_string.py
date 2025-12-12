#!/usr/bin/python3
"""
Module that provides a function to convert a Python object to a JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object.

    Args:
        my_obj: The object to convert.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
