#!/usr/bin/env python3

def safe_print_integer(value):
    txt = "{:d}"
    try:
        print(txt.format(value))
        return (True)

    except ValueError:
        return (False)
