#!/usr/bin/env python3

def print_last_digit(number):

    if number >= 0:
        digit = number % 10
    elif number <= 0:
        digit = (number * -1) % 10
    else:
        digit = 0

    return (digit)
