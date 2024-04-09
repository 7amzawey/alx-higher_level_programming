#!/usr/bin/python3
"""Function that divides all elements of matrix"""

def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.
    
    Args:
        matrix: is the matrix.
        div: is the element that the matrix elements will be divided upon.
    Raises:
        TypeError: if the matrix is not a list of lists and the numbers are,
        not integers or float.
        ZeroDivisionError: if the div is equal to zero.
    Returns:
        a new matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
