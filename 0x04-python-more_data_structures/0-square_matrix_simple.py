#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """squares a matrix

    Args:
        matrix: the matrix to be squared

    Returns:
        the squared matrix
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = (matrix[i][j]) ** 2
    return matrix
