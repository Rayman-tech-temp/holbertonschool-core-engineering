#!/usr/bin/env python3
"""
this is a simple file read code function
"""


def read_file(filename=""):
    """
    this will open a file then print read contents then closes.
    """
    with open(filename, 'r') as file:
        print(file.read(), end='')
    file.close()
