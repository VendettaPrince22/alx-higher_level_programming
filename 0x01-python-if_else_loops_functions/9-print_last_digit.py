#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = number - number - number
        print("{}".format(num % 10), end='')
        return num % 10
    else:
        print("{}".format(number % 10), end='')
        return number % 10
