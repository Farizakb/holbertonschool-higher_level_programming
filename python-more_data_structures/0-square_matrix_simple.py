#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a new matrix with the square of each value."""
    return [list(map(lambda x: x * x, row)) for row in matrix]
