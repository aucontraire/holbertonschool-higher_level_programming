#!/usr/bin/python3


class Matrix:
    """ Matrix."""

    def __init__(self, matrix):
        self.matrix = matrix

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix):
        if not isinstance(matrix, list):
            raise TypeError("m_a must be a list")
        if len(matrix) == 0:
            raise ValueError("m_a can't be empty")
        rows = len(matrix)
        columns = len(matrix[0])
        if columns == 0:
            raise ValueError("m_a can't be empty")
        for r in range(rows):
            if len(matrix[r]) != columns:
                raise TypeError("each row of m_a must should be of the same size")

        for r in range(rows):
            for c in range(columns):
                n = matrix[r][c]
                if not isinstance(n, int) and not isinstance(n, float):
                    raise TypeError("m_a should contain only integers or floats")

        self.__matrix = matrix

    def __len__(self):
        return len(self.__matrix)

    def __getitem__(self, index):
        return self.__matrix[index]


def matrix_mul(m_a, m_b):
    m_a = Matrix(m_a)
    m_b = Matrix(m_b)

    rows_a = len(m_a)
    columns_a = len(m_a[0])
    rows_b = len(m_b)
    columns_b = len(m_b[0])

    if columns_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    row = []
    matrix = []
    for i in range(rows_a):
        for j in range(columns_b):
            sums = 0
            for k in range(rows_b):
                sums = sums + (m_a[i][k] * m_b[k][j])
            row.append(sums)
        matrix.append(row)
        row = []
    return matrix


if __name__ == '__main__':
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
