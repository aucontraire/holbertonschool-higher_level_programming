#!/usr/bin/python3

""" matrix_divided

Divides all elements of a matrix, returns new matrix
Floats get converted to integers, all others raise TypeError
"""


def matrix_divided(matrix, div):
    """ matrix_divided - divides all elements of a matrix
    Returns: new matrix
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        rows = len(matrix)
        columns = len(matrix[0])
        for r in range(rows):
            if len(matrix[r]) != columns:
                raise TypeError("Each row of the matrix must have the same size")

        new_matrix = [[0 for i in range(columns)] for j in range(rows)]
        for r in range(rows):
            for c in range(columns):
                n = matrix[r][c]
                if not isinstance(n, int) and not isinstance(n, float):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    new_matrix[r][c] = float("%0.2f" % (n / div))

        return new_matrix


if __name__ == '__main__':
    matrix = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
