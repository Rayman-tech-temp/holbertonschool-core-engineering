#!/usr/bin/env python3

import add_0
a = 1
b = 2
c = add_0.add(a, b)

if __name__ == "__main__":
    txt = "{a} + {b} = {c}"
    print(txt.format(a, b, c))
