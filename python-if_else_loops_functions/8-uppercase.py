#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase"""
    upper_str = ""
    for c in str:
        if 'a' <= c <= 'z':
            upper_str += chr(ord(c) - 32)
        else:
            upper_str += c
    print("{}".format(upper_str))
