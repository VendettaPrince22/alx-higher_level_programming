#!/usr/bin/python3


def no_c(my_string):
    """Removes all characters c and C from a string
    Args:
        my_string: string to work on
    Return new modified string
    """
    my_list = []
    for letter in my_string:
        #print(letter)
        my_list.append(letter)
        if letter == 'c':
            my_list.remove(letter)
        elif letter == 'C':
            my_list.remove(letter)
    new_string = ''.join([str(elem) for elem in my_list])
    return new_string
