#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list
    Args:
        my_list: list to work with
        idx: index to delete at
    Returns the modified list (original)
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]

    return my_list
