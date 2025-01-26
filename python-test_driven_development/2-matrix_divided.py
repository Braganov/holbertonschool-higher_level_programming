#!/usr/bin/python3
""" Divide a matrix """


def matrix_divided(matrix, div):
    """Returns: new matrix (list of lists)
        Arges:
            matrix: (list of lists)
            div: int
        """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    matrix_lists_len = -1
    # matrix must be a list
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]
