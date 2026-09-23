#!/usr/bin/env python3

def pow(a, b):
    i = 0
    answer = 1
    if a != 0 and b != 0:
        if b > 0:
            for i in range(0, b):
                answer = answer * a
        elif b < 0:
            for i in range(0, b, -1):
                answer = answer / a

    return (answer)
