#!/usr/bin/python3
"""Create a function def pascal_triangle(n): that returns a list of
lists of integers representing the Pascal’s triangle of n:"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # Each row starts with 1

        # Calculate the next values in the row based on the previous row
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])

            row.append(1)  # Each row ends with 1

        triangle.append(row)

    return triangle
