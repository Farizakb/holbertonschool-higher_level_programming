#!/usr/bin/python3
"""
Module that contains a function to check
if an object is an instance of a subclass
(inherited) of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class
    that inherits (directly or indirectly) from a_class,
    otherwise returns False.

    Args:
        obj: Object to check.
        a_class: Class to compare with.

    Returns:
        bool: True if obj is instance of subclass of a_class, False otherwise.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
