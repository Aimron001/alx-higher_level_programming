#!/usr/bin/python3
"""Defines a function for summing commandline args"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        args = load_from_json_file("add_item.json")
    except FileNotFoundError:
        args = []
    items.extend(sys.argv[1:])
    save_to_json_file(args, "add_item.json")
