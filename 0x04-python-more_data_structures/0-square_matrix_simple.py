#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    input_matrix = [[number**2 for number in row] for row in matrix]
    return input_matrix
