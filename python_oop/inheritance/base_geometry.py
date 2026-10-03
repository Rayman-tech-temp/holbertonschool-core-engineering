#!/usr/bin/env python3

class BaseGeometry:
    """
    the details of the functions and attributes, raises tyoe error if not int.
    """
    def __init__(self, __size=0):
        self.size = __size

    def area(self):
        raise Exception("area() is not implemented")

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

    def integer_validator(self, name, value):
        if type(value) is str:
            raise TypeError("{} must be an integer".format(name))
        elif type(value) is float:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.__size = value
