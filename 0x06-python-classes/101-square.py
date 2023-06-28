#!/usr/bin/python3
# """ Defines a square with a size attribute"""


class Square:
    """square class with size attribute

    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @position.setter
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
