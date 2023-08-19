#!/usr/bin/python3
""" defines add function"""


def add_integer(a, b=98):
    """adds 2 integers

    Arguements:
        a (int): First int
        b (int): second int
    Returns: the sum of two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
