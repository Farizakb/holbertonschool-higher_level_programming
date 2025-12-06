#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2."""
    return dict(map(lambda kv: (kv[0], kv[1] * 2), a_dictionary.items()))
