#!/usr/bin/env python3

def safe_print_division(a, b):
    try:
        result = None
        result = a / b
        print("Inside result: {:.1f}".format(result))

        return (result)

    except ZeroDivisionError:
        print("Inside result: {0}".format(None))
        return (None)
