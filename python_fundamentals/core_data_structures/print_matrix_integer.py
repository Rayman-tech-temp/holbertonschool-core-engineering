#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    txt = "{:d}"
    delim = " "
    curline = ""

    if matrix:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j < len(matrix[i]) - 1:
                    curline = curline + txt.format(matrix[i][j]) + delim
                else:
                    curline = curline + txt.format(matrix[i][j])
            print(curline)
            curline = ""
