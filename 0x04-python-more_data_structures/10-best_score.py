#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value
    Args:
        a_dictionary: the dictionary
    Returns:
        a key with the biggest integer value
    """
    if a_dictionary == None:
        return None
    val = 0
    for key in a_dictionary:
       if a_dictionary[key] > val:
           val = a_dictionary[key]
    return val
