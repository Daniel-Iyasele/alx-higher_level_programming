#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """new_matrix = matrix
    return [[new_matrix[i][j] ** 2 for j in range(len(matrix))]
            for i in range(len(matrix[0]))]"""
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
