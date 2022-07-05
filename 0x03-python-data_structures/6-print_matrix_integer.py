#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print(f"{col:d}", sep="", end="")
            if col != row[len(row) - 1]:
                print(" ", end="")
        print()
