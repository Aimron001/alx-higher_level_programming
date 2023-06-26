#!/usr/bin/python3

def magic_calculation(a, b):
    """does some magic calculation

        args:
            a: val 1
            b: val 2
        Returns:
            results of the calculation
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return (result)
