#!/usr/bin/python3
""" this function divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists): The matrix to be divided
        div (int or float): the number to divide

    Returns:
        list of lists: a new matarix

    Raises:
        TypeError: If matrix is not a list of ints or float
        ZeroDivisionError: if div is equal to 0
        TypeError: if each row doesnt have same size
    """
    # validate matrix
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # check if the matrix is empty
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in matrix for num in row]):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # check if each row of the matrix has the same size
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # divide each matrix element by div and round to 2 dp
    new_matrix = [[round(element / div, 2)
                   for element in row] for row in matrix]

    return new_matrix
