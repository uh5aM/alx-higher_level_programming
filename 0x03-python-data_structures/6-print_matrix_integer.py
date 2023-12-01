#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for number in matrix:
            print("{:d}".format(number), end="")
            if(number is not element[len(element)-1]):
                print(" ", add="")
