#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a ifunction that returns JSON-to-object"""
import json


def from_json_string(my_str):
    """Returns the json object representation"""
    return json.loads(my_str)
