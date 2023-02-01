#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [[val**2 for val in row] for row in matrix]
    return square_matrix
