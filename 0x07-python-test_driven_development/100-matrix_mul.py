#!/usr/bin/python3


class Matrix:
    """Matrix.

    Attributes:
        name (str): name of matrix to use for error handling
    """
    name = None

    @classmethod
    def set_name(cls, name, matrix):
        """set_name class method, alternative constructor

        Alternative constructor that provides a way to customize error handling
        messages to include name of matrix

        Args:
            name (str): name of matrix.
            matrix (list): list of lists
        """
        cls.name = name
        return cls(matrix)

    def __init__(self, matrix):
        """__init__ method.

        Args:
            matrix (list): list of lists
        """
        self.matrix = matrix

    @property
    def matrix(self):
        """matrix: returns matrix object

        Args:
            matrix (list): list of lists

        Returns:
            matrix object

        Raises:
            TypeError: if not a list or list of lists, not ints and floats, not
                uniform in row width
            ValueError: if empty or cannot be multiplied
        """
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix):
        if not isinstance(matrix, list):
            raise TypeError("{:s} must be a list".format(Matrix.name))
        if len(matrix) == 0:
            raise ValueError("{:s} can't be empty".format(Matrix.name))
        rows = len(matrix)
        columns = len(matrix[0])
        if columns == 0:
            raise ValueError("{:s} can't be empty".format(Matrix.name))
        for r in range(rows):
            if len(matrix[r]) != columns:
                raise TypeError(
                    "each row of {:s} must should be of the same size".format(
                        Matrix.name))

        for r in range(rows):
            for c in range(columns):
                n = matrix[r][c]
                if not isinstance(n, int) and not isinstance(n, float):
                    raise TypeError(
                        "{:s} should contain only integers or floats".format(
                            Matrix.name))

        self.__matrix = matrix

    def __len__(self):
        """Provides length functionality to matrix object."""
        return len(self.__matrix)

    def __getitem__(self, index):
        """Provides indexing functionality to matrix object."""
        return self.__matrix[index]


def matrix_mul(m_a, m_b):
    """matrix_mul multiplies two matrix objects

    Note:
        Most of the error handling is done in the Matrix class

    Args:
    m_a (Matrix obj):
    m_b (Matrix obj):

    Returns:
        matrix object that is the result of matrix multiplication

    Raises:
        ValueError: if matrices cannot be multiplied
    """
    m_a = Matrix.set_name('m_a', m_a)
    m_b = Matrix.set_name('m_b', m_b)

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
                sums += m_a[i][k] * m_b[k][j]
            row.append(sums)
        matrix.append(row)
        row = []
    return matrix


if __name__ == '__main__':
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
