#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            # print("{}".format(str[i]), end='')
            new = ord(str[i]) - 32
            print(chr(new), end='')
        else:
            print("{}".format(str[i]), end='')

