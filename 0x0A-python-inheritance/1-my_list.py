#!/usr/bin/python3
"""
Contains class MyList that inherits from list
"""
class MyList(list):
    """ Displays the public instance of print """
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
