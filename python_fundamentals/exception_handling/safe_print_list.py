#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    txt = '{0}'
    output = ''
    size = 0
    i = 0
    try:
        for i in my_list:
            size = i
        for i in range(0, x):
            output = output + txt.format(my_list[i])
        print(output)
        return (my_list[i])

    except IndexError:
        if x == 0 and size != 0:
            return (x)
        elif i == size and size != 0:
            print(output)
            return (my_list[i - 1])
        else:
            print("outside of list bounds")
