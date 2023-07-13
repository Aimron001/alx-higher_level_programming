#!/usr/bin/python3
"""Defines a function for checking class."""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match
        Returns:
            True if the object is an instance of the class
            otherwise False:
                """
    if type(obj) == a_class:
        return True
    return False
