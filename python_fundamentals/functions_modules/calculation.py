#!/usr/bin/env python3

from calculator_1 import add, sub, div, mul
a = 10
b = 5
txt = "{0}\n"

if __name__ == "__main__":
    c = add(a, b)
    print(txt.format(c))
    c = sub(a, b)
    print(txt.format(c))
    c = mul(a, b)
    print(txt.format(c))
    c = div(a, b)
    print(txt.foramt(c))
