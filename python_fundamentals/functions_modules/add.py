#!/usr/bin/env python3

from add_0 import add
a = 1
b = 2
c = add(a, b)

if __name__ == "__main__":
    txt = "{0} + {1} = {2}"
    print(txt.format(a, b, c))
