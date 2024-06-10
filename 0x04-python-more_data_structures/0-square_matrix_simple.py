#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix
    Args:
        matrix: matrix to work on
    Returns new matrix modified
    """
    new_matrix = []
    for i in matrix:
        new_list = list(map(lambda x: x ** 2, i))
        new_matrix.append(new_list)

    return new_matrix
