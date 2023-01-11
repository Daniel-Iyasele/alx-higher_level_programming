#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        column_length = len(matrix[0])
        row_length = len(matrix)
        for row in range(row_length):
            for column in range(column_length):
                print("{:d}".format(matrix[row][column]), end="")
                if column < (column_length - 1):
                    print(" ", end="")
                else:
                    print()
    else:
        print()
