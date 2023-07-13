#!/usr/bin/python3
"""Defines an lookup function for attributes."""


def lookup(obj):
    """ returns the list of available attributes and methods of an object:t """
    return (dir(obj))
