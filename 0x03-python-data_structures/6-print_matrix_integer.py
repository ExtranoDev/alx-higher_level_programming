#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [] or matrix != [[]]:
        for i in matrix:
            temp = len(i)
            for j in i:
                print("{:d}".format(j), end='')
                if temp == 1:
                    break
                print(" ", end="")
                temp = temp - 1
            print("")
    else:
        return
