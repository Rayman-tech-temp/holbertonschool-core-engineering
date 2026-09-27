#!/usr/bin/env python3

def element_at(my_list, idx):
    if my_list:
        if idx < len(my_list) and idx >= 0:
            return (my_list[idx])
    else:
        return (None)
