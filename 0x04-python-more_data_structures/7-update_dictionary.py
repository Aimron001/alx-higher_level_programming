#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: the dictionary
        key: string-the key
        value: value to the key
    Returns:
        updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
