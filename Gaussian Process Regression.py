# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:48:13 2020

@author: Grant
"""

import numpy

import math

data = [[1, 1], [2, 3], [5, 6], [8, 9], [15, 16]]

novel_input = [11, 12]

l = 2
v0 = 5

x = []
y = []

for d in data:
    x.append(d[0])
    y.append(d[1])

print(x)
print(y)

x_matrix = numpy.array(x)
y_matrix = numpy.array(y)

N = len(x)

max_likelihood = -1000000000000000000000000000000000
current_max_set = [0, 0]

#learning the optimal parameters
for l_test in range(0, 100):
    for v0_test in range(0, 100):
        l_test = l_test * 0.1
        v0_test = v0_test * 0.1
        
        K = []

        for a in range(len(x)):
            temp = []
            for b in range(len(x)):
                temp.append(v0_test * math.exp(-1/2 * l_test * (x[a] - x[b])**2))
            K.append(temp)
        K_matrix = numpy.array(K)
        
        likelihood_left = numpy.dot(y_matrix.T, numpy.linalg.pinv(K_matrix))
        a_likelihood_left = numpy.dot(likelihood_left, y_matrix)
        print(a_likelihood_left)
        actual_likelihood_left = -1/2 * a_likelihood_left
        
        length = len(K_matrix)
        
        pi_matrix = [[2 * math.pi] * length] * length
        
        likelihood_right = numpy.linalg.det(numpy.multiply(pi_matrix, K_matrix))
        #print("HERE")
        print(likelihood_right)
        if likelihood_right < 0.001:
            continue
        actual_likelihood_right = 1/2 * math.log(likelihood_right)
        
        print()
        print("HERE")
        print(actual_likelihood_left)
        print(actual_likelihood_right)
        print()
        
        likelihood = actual_likelihood_left - actual_likelihood_right
        
        #print("HERE")
        print(likelihood)
        
        if likelihood > max_likelihood:
            current_max_set[0] = l_test
            current_max_set[1] = v0_test
            max_likelihood = likelihood

print("HERE")
print(current_max_set)

l = current_max_set[0]
v0 = current_max_set[1]



K_x_x = []

for a in range(len(x)):
    temp = []
    for b in range(len(x)):
        temp.append(v0 * math.exp(-1/2 * l * (x[a] - x[b])**2))
    K_x_x.append(temp)
K_x_x_matrix = numpy.array(K_x_x)
print("HERE")
print(K_x_x_matrix)




K_x_x_star = []

for a in range(len(x)):
    temp = []
    temp.append(v0 * math.exp(-1/2 * l * (x[a] - novel_input[0])**2))
    K_x_x_star.append(temp)
K_x_x_star_matrix = numpy.array(K_x_x_star)
print(K_x_x_star_matrix)



K_x_star_x_matrix = K_x_x_star_matrix.T
print(K_x_star_x_matrix)


e = v0 * math.exp(-1/2 * l * (novel_input[0] - novel_input[0])**2)
K_x_star_x_star_matrix = numpy.array([e])
print(K_x_star_x_star_matrix)




#calculate Gaussian Distribution
mean = numpy.dot(K_x_star_x_matrix, numpy.linalg.inv(K_x_x_matrix))
mean = numpy.dot(mean, y_matrix)
actual_mean = mean[0]
print(actual_mean)

variance_right = numpy.dot(K_x_star_x_matrix, numpy.linalg.inv(K_x_x_matrix))
variance_right = numpy.dot(variance_right, K_x_x_star_matrix)
#print(variance_right)
actual_variance_right = variance_right[0][0]
#print(actual_variance_right)

variance = K_x_star_x_star_matrix[0] - actual_variance_right
print(variance)

