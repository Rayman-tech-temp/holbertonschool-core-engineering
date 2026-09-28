#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    txt = '{0}'
    output = ''
    try:
        for i in range(0, x):
            output = output + txt.format(my_list[i])
        print(output)

        if x == len(my_list):
            return (my_list[x - 1])
        else:
            return (my_list[x])
    except IndexError:
        print("outside of list bounds")
