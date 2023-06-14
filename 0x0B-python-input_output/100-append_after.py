#!/usr/bin/python3
"""Function that inserts a line of test to a file after each line containing a specific string"""
def append_after(filename="", search_string="", new_string=""):
    """Adds a new line after each line containing aspecific string"""
   text = ""
   with open(filename, 'r', encoding="utf-8") as f:
        for line in r:
            text += line
            if search_string in line:
                text += string
    with open(filename, 'w') as w:
        w.write(text)
