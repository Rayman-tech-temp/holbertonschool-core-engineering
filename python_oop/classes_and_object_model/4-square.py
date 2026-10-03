#!/usr/bin/env python3
"""
Class that is commented
"""


class Square():
    """
    the details of the functions and attributes, raises tyoe error if not int.
    """
    def __init__(self, __size=0):
        self.size = __size

    def area(self):
        return (self.size * self.size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is str:
            raise TypeError("size must be an integer")
        elif type(value) is float:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value
