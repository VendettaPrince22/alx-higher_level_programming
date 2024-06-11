#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys
    Args:
        a_dictionary: dictionary to work with
    """
    sorted_keys = sorted(a_dictionary)
    new_dict = {x: a_dictionary[x] for x in sorted_keys}

    for k, v in new_dict.items():
        print("{:s}: {}".format(k, v))
