#!/usr/bin/env python3

from add_0 import add
a = 1
b = 2
c = add(a, b)

if __name__ == "__main__":
    txt = "{a} + {b} = {c}"
    print(txt.format(a, b, c))
