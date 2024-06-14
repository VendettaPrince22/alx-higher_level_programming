#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists
    Args:
        my_list_1 - list 1; to be divided
        my_list_2 - list 2; used to divide
        list_length - length of list to return
    Return new list
    """
    try:
        new_list = []
        for i in range(list_length):
            try:
                res = my_list_1[i] / my_list_2[i]
                new_list.append(res)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except TypeError:
                print("wrong type")
                new_list.append(0)
            except IndexError:
                print("out of range")
                new_list.append(0)
    finally:
        return new_list
