# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:55:48 2020

@author: Grant
"""

import math
import numpy

X = [[1, 3, 5, 6], [2, 6, 8, 1], [3, 1, 6, 1]]
Y = [61, 59, 40]

n = 3
n_parameters = 4
L = 1

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

temp_I = [n*L, 0, 0], [0, n*L, 0], [0, 0, n*L]
I = numpy.array(temp_I)

matrix_x = numpy.array(X)
matrix_y = numpy.array(Y)
matrix_k = numpy.array(K)

matrix_k = numpy.linalg.inv(numpy.add(matrix_k, I)) 

alpha = numpy.dot(matrix_k, Y)

print(numpy.dot(alpha, matrix_x))