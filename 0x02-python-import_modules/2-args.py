#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1
    if a == 0:
        print("{:d} arguments.".format(a))
    elif a == 1:
        print("{:d} argument:".format(a))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(a))
        for i in range(1, a + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
