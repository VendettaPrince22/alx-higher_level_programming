#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary
    Args:
        a_dictionary: dictionary to work with
        key: key to add or replace
        value: value to add or replace
    Returns modified dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
