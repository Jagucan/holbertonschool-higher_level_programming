#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            for num in row:
                if row is not "\n":
                    if isinstance(num, int):
                        print("{:d}".format(num), end=" ")

            print()
