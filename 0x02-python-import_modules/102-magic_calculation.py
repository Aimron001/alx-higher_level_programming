#!/usr/bin/python3
def magic_calculation(a, b):
    """bytecode function."""
    from magic_calculation_102 import add, sub
    if a < b:
        sumOf = add(a, b)
        for i in range(4, 6):
            sumOf = add(sumOf, i)
        return (sumOf)
    else:
        return (sub(a, b))
