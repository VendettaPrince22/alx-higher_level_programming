#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list
    Args:
        my_list - list to work with
        x - number of elements to print
    """
    try:
        num = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            num += 1
        print("")
        return num

    except IndexError:
        print("")
        return num
