#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 0
    if len(sys.argv) == 1:
        print("{:d}".format(a))
    else:
        for i in range(1, len(sys.argv)):
            a += int(sys.argv[i])
        print("{:d}".format(a))
