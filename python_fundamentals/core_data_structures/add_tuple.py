#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b and len(tuple_b) > 1 and len(tuple_a) > 1:
        outTup = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    elif tuple_a and not tuple_b:
        outTup = tuple_a
    elif not tuple_a and tuple_b:
        outTup = tuple_b
    elif len(tuple_b) == 1 and len(tuple_a) > 1:
        outTup = ((tuple_a[0] + tuple_b[0]), (tuple_a[1]))
    elif len(tuple_a) == 1 and len(tuple_b) > 1:
        outTup = ((tuple_a[0] + tuple_b[0]), (tuple_b[1]))
    else:
        outTup = (0, 0)

    return (outTup)
