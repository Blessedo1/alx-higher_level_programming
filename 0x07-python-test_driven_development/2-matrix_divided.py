#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check that each row has same size
    row_sizes = []
    for i in matrix:
        row_sizes.append(len(i))
    if len(set(row_sizes)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Perform matrix division
    result = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        sub_row = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            sub_row.append(round(j / div, 2))
        result.append(sub_row)
    return result
