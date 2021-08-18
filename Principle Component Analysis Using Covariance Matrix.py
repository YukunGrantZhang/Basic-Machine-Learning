# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:03:31 2020

@author: Grant
"""

import numpy
from scipy import linalg as LA

training_points = [[5, 6], [6, 4], [7, 8], [8, 9], [11, 12], [15, 16]]

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

C = numpy.dot(matrix_X[:].T, matrix_X[:])

e_vals, e_vecs = numpy.linalg.eig(C)

matrix_evecs = numpy.array([e_vecs[0]])
matrix_x = numpy.array(inputs_x)

view_2 = numpy.dot(matrix_evecs[:], matrix_x[:])
print(view_2)

P = numpy.dot(matrix_evecs.T, matrix_evecs)
x_average = len(training_points) * [average]

view_1 = numpy.add(numpy.dot(P[:], matrix_x[:]), x_average)
print(view_1)