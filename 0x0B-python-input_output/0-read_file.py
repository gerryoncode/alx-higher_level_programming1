#!/usr/bin/python3
"""
Function that reads a test file in utf-8 format and prints it to stdout
"""


def read_file(filename=""):
    """ Function takes a filename and reads the data """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
