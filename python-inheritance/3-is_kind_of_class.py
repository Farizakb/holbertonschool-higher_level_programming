#!/usr/bin/python3
"""
Module that contains a function to check
if an object is an instance of, or
inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or
    an instance of a class that inherited from a_class,
    otherwise returns False.

    Args:
        obj: Object to check.
        a_class: Class to compare with.

    Returns:
        bool: True if obj is instance of a_class or subclass, False otherwise.
    """
    return isinstance(obj, a_class)
