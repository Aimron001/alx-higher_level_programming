#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary
    Args:
        a_dictionary: the dictionary
        key: key to delete
    Returns:
        modified dictionary
    """
    if a_dictionary.get(key) is not None:
        a_dictionary.pop(key)
    return a_dictionary
