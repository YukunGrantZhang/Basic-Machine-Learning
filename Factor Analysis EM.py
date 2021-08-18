# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:54:20 2020

@author: Grant
"""

import numpy

import math

data = [[1, 2, 1], [2, 3, 3], [3, 4, 5], [5, 5, 6], [6, 5, 6], [8, 9, 8]]

N = len(data)
noise_length = 3

noise_matrix = []
for m in range(noise_length):
    temp = []
    for n in range(noise_length):
        if m == n:
            temp.append(1)
        else:
            temp.append(0)
    noise_matrix.append(temp)
print(noise_matrix)
actual_noise_matrix = numpy.array(noise_matrix)
print(actual_noise_matrix)

mean = []
sum_x = 0
sum_y = 0
sum_z = 0
for d in data:
    sum_x = sum_x + d[0]
    sum_y = sum_y + d[1]
    sum_z = sum_z + d[2]
mean.append(sum_x / N)
mean.append(sum_y / N)
mean.append(sum_z / N)
print(mean)


variance = []
x_set = []
y_set = []
z_set = []
for d in data:
    x_set.append(d[0])
    y_set.append(d[1])
    z_set.append(d[2])
    
variance.append(numpy.var(x_set))
variance.append(numpy.var(y_set))
variance.append(numpy.var(z_set))
print("HERE")
print(variance)


d_n = []
for d in data:
    temp = []
    temp.append(d[0] - mean[0])
    temp.append(d[1] - mean[1])
    temp.append(d[2] - mean[2])
    d_n.append(temp)
print(d_n)
d_n_matrix = numpy.array(d_n)

converge = False

likelihood = -0.5

convergence_criteria = 0.1

F = []
for b1 in range(noise_length):
    temp = []
    for b2 in range(noise_length):
        temp.append(1)
    F.append(temp)
print(F)
F_matrix = numpy.array(F)

while converge == False:
    previous_F = F_matrix[:]
    previous_noise_matrix = actual_noise_matrix[:]
    
    m_n = []
    
    I = []
    for a1 in range(noise_length):
        temp = []
        for a2 in range(noise_length):
            if a1 == a2:
                temp.append(1)
            else:
                temp.append(0)
        I.append(temp)
    print(I)
    I_matrix = numpy.array(I)
    
    
    m_n_left1 = numpy.dot(numpy.dot(F_matrix.T, numpy.linalg.inv(actual_noise_matrix)), F_matrix)
    print(m_n_left1)
    m_n_left = numpy.linalg.inv(numpy.add(I_matrix, m_n_left1))
    print(m_n_left)
    
    m_n_right = numpy.dot(numpy.dot(F_matrix.T, numpy.linalg.inv(actual_noise_matrix)), d_n_matrix.T)
    print(m_n_right)
    
    m_n = numpy.dot(m_n_left, m_n_right)
    print(m_n)
    
    
    
    
    sigma = []
    
    sigma1 = numpy.dot(numpy.dot(F_matrix.T, numpy.linalg.inv(actual_noise_matrix)), F_matrix)
    print(sigma1)
    sigma = numpy.linalg.inv(numpy.add(I_matrix, sigma1))
    print(sigma)
    
    
    
    
    A = []
    
    A1 = numpy.dot(d_n_matrix.T, m_n.T)
    print(A1)
    
    N_1 = []
    for w1 in range(noise_length):
        temp = []
        for w2 in range(noise_length):
            temp.append(1 / N)
        N_1.append(temp)
    print(N_1)
    
    A = numpy.multiply(N_1, A1)
    print(A)
    
    
    
    H = []
    H_right = numpy.multiply(N_1, numpy.dot(m_n, m_n.T))
    print(H_right)
    H = numpy.add(sigma, H_right)
    print(H)
    
    
    
    F_matrix = numpy.dot(A, numpy.linalg.inv(H))
    print(F_matrix)
    
    
    
    
    noise_1 = numpy.multiply(N_1, numpy.dot(d_n_matrix.T, d_n_matrix))
    print(noise_1)
    
    double = []
    for e1 in range(noise_length):
        temp = []
        for e2 in range(noise_length):
            temp.append(2)
        double.append(temp)
    print(double)
    
    noise_2 = numpy.multiply(double, numpy.dot(F_matrix, A.T))
    print(noise_2)
    
    noise_3 = numpy.dot(numpy.dot(F_matrix, H), F_matrix.T)
    print(noise_3)
    
    noise = numpy.add(numpy.subtract(noise_1, noise_2), noise_3)
    print(noise)
    
    for u in range(noise_length):
        temp = []
        for v in range(noise_length):
            if u == v:
                noise_matrix[u][v] = noise[u][v]
    actual_noise_matrix = numpy.array(noise_matrix)
    print(actual_noise_matrix)
    print(previous_noise_matrix)
    
    
    converge = True
    
    for r1 in range(noise_length):
        for r2 in range(noise_length):
            if r1 == r2:
                if abs(actual_noise_matrix[r1][r2] - previous_noise_matrix[r1][r2]) > convergence_criteria:
                    converge = False
    
    

            
    