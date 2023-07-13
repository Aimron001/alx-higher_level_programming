#!/usr/bin/python3
"""Defines a class and inheritis the class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if a an object is an instance of a class

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of object to.
    Returns:
        True - if the obj is an instance
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
