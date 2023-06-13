#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Load object form a json file"""
    with open(filename, 'r') as f:
        """opens the file"""
        return json.load(f)
