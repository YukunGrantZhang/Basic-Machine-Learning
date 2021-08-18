# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:27:34 2020

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
            summation += gaussian_kernel(X[i][j], X[k][j], 1) / (gaussian_kernel(X[i][j], X[i][j], 1) * gaussian_kernel(X[k][j], X[k][j], 1))**(1/2)
        temp_k.append(summation)
    
    K.append(temp_k)

temp_I = [[1/n, 1/n, 1/n], [1/n, 1/n, 1/n], [1/n, 1/n, 1/n]]
I = numpy.array(temp_I)
K = numpy.array(K)

K1 = numpy.subtract(K[:], numpy.dot(I[:], K[:]))
K1 = numpy.subtract(K1[:], numpy.dot(K[:], I[:]))
K1 = numpy.add(K1[:], numpy.dot(numpy.dot(I[:].T, K[:]), I[:]))

matrix_x = numpy.array(X)
matrix_y = numpy.array(Y)

alpha = numpy.dot(numpy.linalg.pinv(K1), Y)

print(numpy.dot(alpha, matrix_x))