#!/usr/bin/python3
""" defines a Base class """


class Base:
    """represents the Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
