#!/usr/bin/python3
"""
Function that returns a list of available attributes and methods
"""
def lookup(obj):
   """Returns the list of attributes"""
    return dir(obj)
