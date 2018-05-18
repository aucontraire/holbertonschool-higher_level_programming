#!/usr/bin/python3


def pascal_triangle(n):
    """Pascal triangle
    Args:
        n (int): number of rows
    Returns:
        matrix representing Pascal's triangle
    """
    matrix = []
    if n <= 0:
        return matrix
    else:
        for r in range(n):
            if r == 0:
                matrix.append([1])
            elif r == 1:
                matrix.append([1, 1])
            else:
                matrix.append([1 for x in range(r + 1)])
                for c in range(1, len(matrix[r]) - 1):
                    matrix[r][c] = matrix[r - 1][c - 1] + matrix[r - 1][c]

    return matrix


if __name__ == '__main__':
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(8))
