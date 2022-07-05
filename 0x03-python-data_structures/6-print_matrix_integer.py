#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), sep="", end="")
            if col != row[len(row) - 1]:
                print(" ", end="")
        print()
