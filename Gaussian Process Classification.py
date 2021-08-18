# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:48:13 2020

@author: Grant
"""

import numpy

import math

data = [[1, 1, 0], [2, 3, 0], [1, 3, 0], [8, 1, 1], [9, 1, 1], [8, 2, 1]]

novel_input = [9, 5, 1]

gamma = 2

x = []
y = []
c = []
s = []

for d in data:
    x.append(d[0])
    y.append(d[1])
    c.append(d[2])
    s.append(1/(1 + math.exp(-d[1])))

print(x)
print(y)
print(c)
print(s)

x_matrix = numpy.array(x)
y_matrix = numpy.array(y)
c_matrix = numpy.array(c)
s_matrix = numpy.array(s)

N = len(x)

D = []

for a in range(N):
    temp = []
    for b in range(N):
        if a == b:
            temp.append(s[a] * (1 - s[a]))
        else:
            temp.append(0)
    D.append(temp)
print(D)
D_matrix = numpy.array(D)

max_likelihood = -1000000000000000000000000000000000
current_max_set = [0]
y_bar_max = []

#learning the optimal parameters
for gamma_test in range(0, 800):
    gamma_test = gamma_test * 0.001
        
    K = []

    for a in range(len(x)):
        temp = []
        for b in range(len(x)):
            temp.append(2 * math.exp((abs(x[a] - x[b]))**gamma_test))
        K.append(temp)
    K_matrix = numpy.array(K)
        
    c_s = numpy.subtract(c_matrix, s_matrix)
        
    y_bar = numpy.dot(K_matrix, c_s)
    y_bar_list = []
    for e in range(len(y_bar)):
        y_bar_list.append(y_bar[e])
    #print(y_bar)
    #print("HERE")
    #print(y_bar_list)
        
    likelihood_1 = numpy.dot(c_matrix.T, y_bar)
    #print(likelihood_1)
        
    likelihood_2 = 0
    for n in range(N):
        likelihood_2 = likelihood_2 + math.log(1 + math.exp(y_bar_list[n]))
    #print(likelihood_2)
        
    likelihood_3_first = numpy.dot(y_bar.T, numpy.linalg.pinv(K_matrix))
    likelihood_3 = 1/2 * numpy.dot(likelihood_3_first, y_bar)
    #print(likelihood_3)
        
    Identity = []
    for r in range(N):
        temp = []
        for u in range(N):
            if r == u:
                temp.append(1)
            else:
                temp.append(0)
        Identity.append(temp)
    #print(Identity)
    Identity_matrix = numpy.array(Identity)
        
    likelihood_4_first = numpy.add(Identity_matrix, numpy.dot(K_matrix, D_matrix))
    likelihood_4_second = numpy.linalg.det(likelihood_4_first)
    if likelihood_4_second < 0.01:
        continue
    likelihood_4 = 1/2 * math.log(likelihood_4_second)
    #print(likelihood_4)
        
    likelihood = likelihood_1 - likelihood_2 - likelihood_3 - likelihood_4
    print(likelihood)
        
    if likelihood > max_likelihood:
        current_max_set[0] = gamma_test
        y_bar_max = y_bar_list[:]
        max_likelihood = likelihood

print(current_max_set)
print(y_bar_max)

gamma = current_max_set[0]


K_x_x = []

for a in range(len(x)):
    temp = []
    for b in range(len(x)):
        temp.append(2 * math.exp((abs(x[a] - x[b]))**gamma))
    K_x_x.append(temp)
K_x_x_matrix = numpy.array(K_x_x)
print("HERE")
print(K_x_x_matrix)

K_x_x_star = []

for a in range(len(x)):
    temp = []
    temp.append(2 * math.exp((abs(x[a] - novel_input[0]))**gamma))
    K_x_x_star.append(temp)
K_x_x_star_matrix = numpy.array(K_x_x_star)
print(K_x_x_star_matrix)



K_x_star_x_matrix = K_x_x_star_matrix.T
print(K_x_star_x_matrix)


e = 2 * math.exp((abs(novel_input[0] - novel_input[0]))**gamma)
K_x_star_x_star_matrix = numpy.array([e])
print(K_x_star_x_star_matrix)


#calculate Gaussian Distribution
s_bar = []
for y in y_bar_max:
    s_bar.append(1 / (1 + math.exp(-y)))
print(s_bar)
s_bar_matrix = numpy.array(s_bar)

mean = numpy.dot(K_x_star_x_matrix, numpy.subtract(c_matrix, s_bar_matrix))
print(mean[0])

variance_right_first = numpy.linalg.inv(numpy.add(K_x_x_matrix, numpy.linalg.inv(D_matrix)))
variance_right = numpy.dot(K_x_star_x_matrix, numpy.dot(variance_right_first, K_x_x_star_matrix))
#print(variance_right)
variance = K_x_star_x_star_matrix[0] - variance_right[0][0]
print(variance)

