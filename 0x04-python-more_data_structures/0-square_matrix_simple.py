#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix is not None:
        rows = len(matrix)
        columns = len(matrix[0])
        if columns != 0:
            sq_matrix = [[0 for i in range(rows)] for j in range(columns)]
            for r in range(rows):
                for c in range(columns):
                    sq_matrix[r][c] = matrix[r][c] ** 2

            return sq_matrix
    else:
        return None


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
