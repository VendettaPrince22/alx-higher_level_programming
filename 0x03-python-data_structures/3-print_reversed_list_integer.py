#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order
    Args:
        my_list: list to reverse
    Return value: reversed list
    """
    new_list = []
    new_list = my_list.copy()
    count = len(new_list)
    for num in range(count):
        print("{:d}".format(my_list.pop()))
