#!/usr/bin/python3
"""
Module that contains a function to check
if an object is exactly an instance of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class,
    otherwise returns False.

    Args:
        obj: Object to check.
        a_class: Class to compare with.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
