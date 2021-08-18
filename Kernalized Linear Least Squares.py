# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:14:07 2020

@author: Grant
"""

import math
import numpy

X = [[1, 3, 5, 6], [2, 6, 8, 1], [3, 1, 6, 1]]
Y = [61, 59, 40]

n = 3
n_parameters = 4

def gaussian_kernel(x_i, x_j, sigma):
    answer = math.exp(-(abs(x_i - x_j))**2 / (2 * sigma**2))
    
    return answer

K = []
for i in range(n):
    temp_k = []
    for k in range(n):
        summation = 0
        for j in range(n_parameters):
            summation += gaussian_kernel(X[i][j], X[k][j], 1)
        temp_k.append(summation)
    
    K.append(temp_k)

matrix_x = numpy.array(X)
matrix_y = numpy.array(Y)
matrix_k = numpy.array(K)

alpha = numpy.dot(numpy.linalg.inv(matrix_k), Y)

print(numpy.dot(alpha, matrix_x))
            