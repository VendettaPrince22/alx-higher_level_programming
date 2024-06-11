#!/usr/bin/python3


def weight_average(my_list=[]):
    """Returns the weighted average of all integers
    Args:
        my_list: list to work with
    Return a number, weighted average
    tuple(<score>, <weight>)
    """
    new_list = list(map(lambda x: x[0] * x[1], my_list))
    sum = 0
    for i in new_list:
        sum += i

    new_list1 = list(map(lambda x: x[1], my_list))
    sum1 = 0
    for i in new_list1:
        sum1 += i

    return sum / sum1
