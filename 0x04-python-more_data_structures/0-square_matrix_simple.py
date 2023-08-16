#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ''' computes square value integers of a matrix'''
    return [list(map((lambda x:x**2), row))for row in matrix]
