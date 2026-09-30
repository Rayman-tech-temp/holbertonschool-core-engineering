#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    size = 0
    i = 0
    count = 0
    try:
        for i in my_list:
            size = i

        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            count = count + 1

        if x != 0:
            print("\n", end="")
        return (count)

    except ValueError:
        for i in range(i, x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
        print("\n", end="")
        return (count)
