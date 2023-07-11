#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    txt = ""
    with open(filename) as fr:
        for line in fr:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as fw:
        fw.write(txt)
