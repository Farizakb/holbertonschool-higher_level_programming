#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in the list."""
    unique_numbers = set(my_list)
    total = 0
    for n in unique_numbers:
        total += n
    return total
