#!/usr/bin/python3
"""Holds the function 'matrix_divided' that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number
    Args:
        matrix (list of lists): matrix to work with
        div (int/float): number to use as divisor
    Returns:
        new modified matrix
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for k in matrix:
        if type(k) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for x in k:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix\
                                (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for i in matrix:
        new_list = []
        for j in i:
            new_list.append(round(j / div, 2))
        new_matrix.append(new_list)

    return new_matrix
