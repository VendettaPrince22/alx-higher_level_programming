#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first n elements of a list and only integers
    Args:
        my_list - list to work with
        x - number of elements to print
    """
    try:
        count = 0
        num = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[count]), end="")
                count += 1
                num += 1
            except (ValueError, TypeError):
                count += 1
        print("")
        return num
    except TypeError:
        pass
