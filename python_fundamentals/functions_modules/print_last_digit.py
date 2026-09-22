#!/usr/bin/env python3

def print_last_digit(number):
    newstr = '{0}'
    if number >= 0:
        digit = number % 10
    else:
        digit = (number * -1) % 10

    print(newstr.format(digit))
