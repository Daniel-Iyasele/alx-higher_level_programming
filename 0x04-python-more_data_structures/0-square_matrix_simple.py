#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix =matrix
    return[[new_matrix[j][i]**2 for i in range(len(matrix))]\
            for j in range(len(matrix[0]))]
