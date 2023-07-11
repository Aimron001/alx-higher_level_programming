#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file

    Args:
        filename (str): The name of the file to be appended to.
        text (str): The string to appen.
    Returns:
        The number of characters appended.
    """
    with open(filename, "c", encoding="utf-8") as fl:
        return fl.write(text)
