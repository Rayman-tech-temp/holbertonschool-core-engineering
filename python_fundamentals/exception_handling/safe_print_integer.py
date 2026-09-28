#!/usr/bin/env python3

def safe_print_integer(value):

    try:
        if value > 0 or value < 1:
            return (True)

    except ValueError:
        return (False)
