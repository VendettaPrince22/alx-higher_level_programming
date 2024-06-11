#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary
    Args:
        a_dictionary: dictionary to work with
    """
    dict_tuple = a_dictionary.items()
    mod_list = list(filter(lambda x: x[1] == value,
                           map(lambda y: y, dict_tuple)))

    key_list = list(map(lambda x: x[0], map(lambda y: y, mod_list)))

    for i in key_list:
        del a_dictionary[i]

    return a_dictionary
