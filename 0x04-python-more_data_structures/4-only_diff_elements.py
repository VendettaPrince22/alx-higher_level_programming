#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set
    Args:
        set_1: first set
        set_2: second set
    """
    set_3 = set_1 ^ set_2

    return set_3
