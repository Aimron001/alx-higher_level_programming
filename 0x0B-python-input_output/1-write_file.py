#!/usr/bin/python3
"""Definees a function for writing to a file"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)

    Args:
        filename (str): name of the file to edit
        text (str): text to be writtn to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
