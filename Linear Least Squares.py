# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:23:54 2020

@author: Grant
"""

import numpy

X = numpy.array([[1, 3, 5], [2, 6, 8], [3, 1, 6]])
Y = numpy.array([[45], [78], [56]])

w_1 = numpy.linalg.inv(numpy.dot(X.T, X)) 
w_2 = numpy.dot(X.T, Y)
w = numpy.dot(w_1, w_2)
print("The weights are:", w[0], w[1], w[2])
