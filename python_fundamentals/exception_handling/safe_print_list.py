#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    txt = '{0}'
    output = ''
    i = 0
    try:
        for i in range(0, x):
            output = output + txt.format(my_list[i])
        print(output)
        return (my_list[x])
    except IndexError:
        if x - 1 == i:
            return (my_list[x - 1])
        else:
            print("outside of list bounds")
