#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda squared_val:
        list(map(lambda int_ma: int_ma ** 2, squared_val)), matrix))
