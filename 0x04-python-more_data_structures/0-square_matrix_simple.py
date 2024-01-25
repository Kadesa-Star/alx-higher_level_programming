#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    final_matrix = []
    for row in matrix:
        sq_row = [elem ** 2 for elem in row]
        final_matrix.append(sq_row)

    return (final_matrix)
