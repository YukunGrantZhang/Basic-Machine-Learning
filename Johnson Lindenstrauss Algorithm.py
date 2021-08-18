# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:46:56 2020

@author: Grant
"""

import math
import random
import numpy

numbers = [-1, 1]

X = [[1, 2, 3], [1, 3, 5], [1, 2, 3], [1, 2, 5], [1, 2, 4], [1, 2, 3], [1, 2, 3], [1, 2, 4], [2, 2, 3], [1, 2, 3], [2, 3, 3], [2, 3, 5], [2, 3, 6], [2, 3, 8], [2, 5, 3], [6, 3, 3], [2, 3, 8], [2, 3, 1], [2, 3, 2], [2, 3, 3], [2, 3, 5], [3, 3, 1], [2, 3, 5]]

B = 0.01
e = 0.95
n = 3
d = len(X)

k = int(math.log(n, 10) * (4 + 2 * B) / (e**2 / 2 - e**3 / 3))

R = []
for i in range(k):
    temp = []
    for j in range(d):
        temp.append(random.choice(numbers))
    R.append(temp)

matrix_X = numpy.array(X)
matrix_R = numpy.array(R)

Y = numpy.dot(R, X)

Y_result = []
for i in range(len(Y)):
    temp = []
    for j in range(len(Y[i])):
        temp.append(Y[i][j] / (k)**(1/2))
    Y_result.append(temp)

print(Y_result)
        

