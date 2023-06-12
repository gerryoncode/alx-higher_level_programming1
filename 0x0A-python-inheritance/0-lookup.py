#!/usr/bin/python3
"""
    Function that returns a list of available attributes and methods
"""
def lookup(obj):
    attributes = []
    methods = []

    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)

        if not callable(attr_value):
            attributes.append(attr_name)
        else: 
            attributes.append(attr_name)
    return attributes
