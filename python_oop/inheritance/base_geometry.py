#!/usr/bin/env python3
"""
Base Geometry class - a lot shapes will become this...
"""


class BaseGeometry:
    """
    the details of the functions and attributes, raises tyoe error if not int.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is str:
            raise TypeError("{} must be an integer".format(name))
        elif type(value) is float:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.__size = value
