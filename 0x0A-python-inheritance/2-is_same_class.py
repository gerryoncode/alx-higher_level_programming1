#!/usr/bin/python3
""" Checks whether an ibject is exactly an instance of the specified class """
def is_same_class(obj, a_class):
    """Function that checks"""
    if isinstance(obj, a_class):
        return True
    else:
        False
