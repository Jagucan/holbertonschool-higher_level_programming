#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers 
        representing the Pascal’s triangle of n 
    """
    if n <= 0:
        return []
    else:
        p = []
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = p[i-1][j-1] + p[i-1][j]
            p.append(row)
        return p
