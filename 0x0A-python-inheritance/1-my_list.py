#!/usr/bin/python3
"""Defines class that inherits the ist caclass"""


class MyList(list):
    """represents a myliast class"""

    def print_sorted(self):
        """Print the list in  ascending order."""
        print(sorted(self))
