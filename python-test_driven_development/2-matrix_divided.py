#!/usr/bin/python3
""" The function divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ The function divides all elements of a matrix if is a number.

    Args:
        matrix (int, float): It's a list of lists.
        div (int, float): It's a number, must be different from 0.

    Returns:
        Returns a new matrix whit the result of a division.
    """


    if type(matrix) is not list \
        or not all(map(lambda x: type(x) is list, matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of \
            integers/floats")

    if not all(map(lambda x: all\
        (map(lambda y: type(y) in [int, float], x)), matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of \
            integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])

    if not all(map(lambda x: len(x) == row_len, matrix)):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(y / div, 2) for y in x] for x in matrix]
