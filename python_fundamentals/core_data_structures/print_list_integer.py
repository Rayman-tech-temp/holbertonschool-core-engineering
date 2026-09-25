#!/usr/bin/env python3

def print_list_integer(a_list):
    txt = "{:d}"
    if a_list:
        for i in a_list:
            print(txt.format(i))
