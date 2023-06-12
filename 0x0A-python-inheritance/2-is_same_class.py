#!/usr/bin/python3
""" Checks whether an ibject is exactly an instance of the specified class """
def is_same_class(obj, a_class):
    """Function that checks"""
    if isinstance(obj, a_class):
       """Checks if the obj is an instance of the a_class"""
        return True
    else:
        return False
