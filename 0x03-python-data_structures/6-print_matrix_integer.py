#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row is not None:
            line = ""
        for i in range(len(row)):
            if i == 0:
                line += "{}"
            else:
                line += " {}"
        print(line.format(*row))
