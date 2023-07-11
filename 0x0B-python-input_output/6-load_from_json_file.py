#!/usr/bin/python3
"""Defines function that creates an Object from a “JSON file”:"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename) as fl:
        return json.load(fl)
