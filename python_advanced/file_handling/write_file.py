#!/usr/bin/env python3
"""
this is a simple file read code function
"""


def write_file(filename="", text=""):
    """
    this will open a file then overwrite the text contents then closes.
    """
    with open(filename, 'r+') as file:
        text = str(text)
        return (file.write(text))
    file.close()
