#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """executes a function safely.

    Args:
        fct: pointer to a function
        args: Arguments for function fct.

    Returns:
        result of the function
        If an error occurs - None.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
