#!/usr/bin/env python3
"""
Class that is commented
"""


class Square():
    """
    the details of the functions and attributes, raises tyoe error if not int.
    """
    def __init__(self, __size=0):
        if type(__size) is str:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = __size
