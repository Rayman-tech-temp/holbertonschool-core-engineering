#!/usr/bin/env python3

from calculator_1 import add, sub, div, mul
a = 10
b = 5

if __name__ == "__main__":
    txt = "{0} + {1} = {2}\n"
    c = add(a, b)
    print(txt.format(a, b, c))

    txt = "{0} - {1} = {2}\n"
    c = sub(a, b)
    print(txt.format(a, b, c))

    txt = "{0} '*' {1} = {2}\n"
    c = mul(a, b)
    print(txt.format(a, b, c))

    txt = "{0} '/' {1} = {2}\n"
    c = div(a, b)
    print(txt.foramt(a, b, c))
