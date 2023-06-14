#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds all unique integers in a list

    Args:
        matrix: the matrix containing the integers

    Returns:
        sum of unique values
    """
    uniq_values = set(my_list)
    sum = 0
    for val in uniq_values:
        sum += val
    return sum
