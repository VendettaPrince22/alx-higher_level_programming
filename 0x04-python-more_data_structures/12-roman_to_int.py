#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts a roman numeral to an integer
    Args:
        roman_string: string containing the roman numeral
    Returns a number from roman numeral
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    num = 0
    my_list = []

    if roman_string is None or type(roman_string) is not str:
        return 0

    for i in roman_string:
        my_list.append(roman_dict[i])

    for j in my_list:
        if j > num:
            num = -num + j
        else:
            num += j

    return num
