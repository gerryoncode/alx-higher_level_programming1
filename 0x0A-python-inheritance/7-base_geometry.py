#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """ This is the class """
    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not type(value) == int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
