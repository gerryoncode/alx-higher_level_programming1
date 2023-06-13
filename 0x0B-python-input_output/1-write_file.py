#!/usr/bin/python3
"""Writest a string to a text file and returns number of charaters written"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
    return f.write(text)
