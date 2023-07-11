#!/usr/bin/python3
"""Defines a function that writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation."""
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
