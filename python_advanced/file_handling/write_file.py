#!/usr/bin/env python3
"""
this is a simple file read code function
"""


def write_file(filename="", text=""):
    """
    this will open a file then print read contents then closes.
    """
    with open(filename, 'w') as file:
        file.write(text)
    file.close()
