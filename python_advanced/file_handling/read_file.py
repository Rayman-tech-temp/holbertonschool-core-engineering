#!/usr/bin/env python3
"""
this is a simple file read code function
"""


def read_file(filename=""):
    with open(filename, 'r') as file:
        print(file.read(), end='')
    file.close()
