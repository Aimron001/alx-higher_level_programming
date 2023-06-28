#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other_square):
        """ the == comparision to a Square."""
        return self.area() == other_square.area()

    def __ne__(self, other_square):
        """Definition of the != comparison to a Square."""
        return self.area() != other_square.area()

    def __lt__(self, other_square):
        """Definition of  the < comparison to a Square."""
        return self.area() < other_square.area()

    def __le__(self, other_square):
        """Definition of the the <= comparison to a Square."""
        return self.area() <= other_square.area()

    def __gt__(self, other_square):
        """Definition of the > comparison to a Square."""
        return self.area() > other_square.area()

    def __ge__(self, other_square):
        """Definition of the >= comparison to a Square."""
        return self.area() >= other_square.area()
