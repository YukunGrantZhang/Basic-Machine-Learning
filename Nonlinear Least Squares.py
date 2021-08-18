# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:45:36 2020

@author: Grant
"""

import numpy

input_data = [[1, 5, 6], [2, 8, 9], [6, 5, 8]]

temp_X = []
for a in input_data:
    temp_entry = []
    temp_entry.append(a[0]**3)
    temp_entry.append(a[1]**2)
    temp_entry.append(a[2])
    temp_X.append(temp_entry)

X = numpy.array(temp_X)
Y = numpy.array([[86], [241], [1163]])

w_1 = numpy.linalg.inv(numpy.dot(X.T, X)) 
w_2 = numpy.dot(X.T, Y)
w = numpy.dot(w_1, w_2)
print("The weights are:", w[0], w[1], w[2])