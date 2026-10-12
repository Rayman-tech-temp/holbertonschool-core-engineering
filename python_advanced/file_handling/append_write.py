#!/usr/bin/env python3
"""
this is a simple file read code function
"""


def append_write(filename="", text=""):
    """
    this will open a file then overwrite the text contents then closes.
    """
    with open(filename, 'a') as file:
        text = str(text)
        output = file.write(text)
    file.close()
    return (output)
