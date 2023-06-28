#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Circle class"""

    def __init__(self, radius=0):
        """Initialize a Magic Circle Class.

        Arg:
            radius (float): The radius of the new circle MagicClass.
        """
        self.__radius = 0
        if not (isinstance(radius, int) and isinstance(radius, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

        def area(self):
            """Returns the  area of the magic class"""
            return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns The circumference of the circle MagicClass."""
        return (2 * math.pi * self.__radius)
