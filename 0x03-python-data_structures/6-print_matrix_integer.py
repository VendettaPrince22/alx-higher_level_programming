#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers
    Args:
        matrix: list with list
    """
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=" ")
        print("")
