#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        row = " ".join("{:d}".format(num) for num in matrix[i])
        print(row)      
