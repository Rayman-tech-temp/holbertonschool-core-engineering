#!/usr/bin/env python3
"""
this is a simple file read code function
"""


def write_file(filename="", text=""):
    """
    this will open a file then overwrite the text contents then closes.
    """
    with open(filename, 'w') as file:
        text = str(text)
        output = file.write(text)
    file.close()
    return (output)
