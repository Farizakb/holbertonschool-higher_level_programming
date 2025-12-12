#!/usr/bin/python3
"""Pascal's Triangle module.
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle of n rows.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list[list[int]]: Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Construct the new row
        row = [1]  # First element
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Last element
        triangle.append(row)

    return triangle
