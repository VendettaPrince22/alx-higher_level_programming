#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value
    Args:
        a_dictionary: dictionary to work with
    Return a number
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    new_list = []
    val = 0
    for k, v in a_dictionary.items():
        if v > val:
            new_list.append(k)
            val = v

    return new_list[-1]
