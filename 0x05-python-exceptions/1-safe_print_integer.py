#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
        value: integer to be printed.
    Returns:
        Returns True if value is an integer
        Otherwise, returns False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
