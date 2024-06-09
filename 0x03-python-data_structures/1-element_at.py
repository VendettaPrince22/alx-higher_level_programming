#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list like in C

    Args:
        my_list: list to retrieve elements from
        idx: index to retrieve element

    The return element is. retrieved element
    """
    if idx < 0:
        return None
    elif idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]
