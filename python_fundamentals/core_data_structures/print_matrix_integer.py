#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    txt = "{:d}"
    delim = " "
    curline = ""
    if matrix:
        for i in range(0, 3):
            for j in range(0, 3):
                curline = curline + txt.format(matrix[i][j]) + delim
            print(curline)
            curline = ""
