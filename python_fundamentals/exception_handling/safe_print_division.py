#!/usr/bin/env python3

def safe_print_division(a, b):
    try:
        result = None
        result = a / b
        print("Inside result: {:.1f}".format(result))

    except ZeroDivisionError:
        result = None
        print("Inside result: {0}".format(result))

    finally:
        return (result)
