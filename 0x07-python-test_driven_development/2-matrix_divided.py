#!/usr/bin/python3
"""
This module contains the function matrix_divided
"""


def matrix_divided(matrix, div):
    """
This function divide the elements of a matrix by a given number

Args:
    matrix(list): the matrix as a list of list
    div(int): the number to divide the elements of the matrix to

Return:
    A new matrix divided
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    new_mat = []
    init_len = len(matrix[0])
    for row in matrix:
        new_row = []
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        this_len = len(row)
        if this_len != init_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) != int and type(item) != float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_row.append(round(item / div, 2))
        new_mat.append(new_row)
    return new_mat
