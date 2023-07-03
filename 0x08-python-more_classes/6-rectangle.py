#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        number_of_instances += 1

    @property
    def width(self):
        "Gets the width"
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return (self.__height)

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the area of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return the area representation of the area Rectangle.

        Represents the rectangle with series "#" character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        area_str = []
        for i in range(self.__height):
            [area_str.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                area_str.append("\n")
        return ("".join(area_str))

    def __repr__(self):
        """Returns string representation of the Rectangle."""
        area_rect = "Rectangle(" + str(self.__width)
        area_rect += ", " + str(self.__height) + ")"
        return (area_rect)

    def __del__(self):
        """prints bye rectangle when an object is deleted"""
        print("Bye rectangle...")
        number_of_instances = number_of_instances - 1
