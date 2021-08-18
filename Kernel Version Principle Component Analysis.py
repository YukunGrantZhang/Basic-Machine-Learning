# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:20:19 2020

@author: Grant
"""

import numpy
from scipy import linalg as LA

training_points = [[5, 6], [6, 4], [7, 8], [8, 9], [11, 12], [15, 16]]

n = len(training_points)

summation = 0
for i in training_points:
    summation += i[0]
average = summation / len(training_points)

X = []
p1 = []
p2 = []
for j in training_points:
    temp = []
    temp.append(j[0] - average)
    p1.append(j[0] - average)
    temp.append(j[1])
    p2.append(j[1])
    X.append(temp)

inputs_x = []
inputs_x.append(p1)
inputs_x.append(p2)

matrix_X = numpy.array(X)

K = numpy.dot(matrix_X[:], matrix_X[:].T)

temp_I = [[1/n, 1/n, 1/n, 1/n, 1/n, 1/n], [1/n, 1/n, 1/n, 1/n, 1/n, 1/n], [1/n, 1/n, 1/n, 1/n, 1/n, 1/n], [1/n, 1/n, 1/n, 1/n, 1/n, 1/n], [1/n, 1/n, 1/n, 1/n, 1/n, 1/n], [1/n, 1/n, 1/n, 1/n, 1/n, 1/n]]
I = numpy.array(temp_I)

K1 = numpy.subtract(K[:], numpy.dot(I[:], K[:]))
K1 = numpy.subtract(K1[:], numpy.dot(K[:], I[:]))
K1 = numpy.add(K1[:], numpy.dot(numpy.dot(I[:].T, K[:]), I[:]))

e_vals, e_vecs = numpy.linalg.eig(K1[:])

V = []
for v in e_vecs[0]:
    V.append(v/(e_vals[0])**(1/2))

print(numpy.dot(V, K1[:]))