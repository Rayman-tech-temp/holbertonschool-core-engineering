#!/usr/bin/env python3

def safe_print_integer(value):
    txt = "{:d}"

    try:
        print(txt.format(value))

    except ValueError:
        print("stop putting other symbols here asshole!")
