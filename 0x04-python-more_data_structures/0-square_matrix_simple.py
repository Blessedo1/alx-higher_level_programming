#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        sub_matrix = []
        for j in i:
            sub_matrix.append(j**2)
        new_matrix.append(sub_matrix)
    return new_matrix
