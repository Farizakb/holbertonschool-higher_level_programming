#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element at a specific index without modifying """
    new_list = my_list[:]  # create a copy of the list
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
