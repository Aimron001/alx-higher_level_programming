#!/usr/bin/python3
"""Defines an inherited function of checking class."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance inherited from a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of object to.
    Returns:
        True if the object is an instance inherited
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
