#!/usr/bin/env python3

def pow(a, b):
    i = 0
    answer = 1
    if a != 0 and b != 0:
        for i in range(0, b):
            answer = answer * a

    print(answer, end='')
    return (answer)
