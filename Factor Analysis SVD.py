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


centre_x = []
for d in data:
    temp = []
    temp.append(d[0] - mean[0])
    temp.append(d[1] - mean[1])
    temp.append(d[2] - mean[2])
    centre_x.append(temp)
print(centre_x)

converge = False

likelihood = -0.5

convergence_criteria = 0.1

while converge == False:
    
    previous_likelihood = likelihood
    
    new_noise_matrix = []
    for a in range(len(noise_matrix)):
        temp = []
        for b in range(len(noise_matrix[a])):
            if a == b:
                temp.append(1 / math.sqrt(noise_matrix[a][b]))
            else:
                temp.append(0)
        new_noise_matrix.append(temp)
    print(new_noise_matrix)
    
    """
    for a in range(len(noise_matrix)):
        for b in range(len(noise_matrix[a])):
            if noise_matrix[a][b] != 0:
                noise_matrix[a][b] = 1 / math.sqrt(noise_matrix[a][b])
    print(noise_matrix)
    """
    actual_noise_matrix = numpy.array(new_noise_matrix)
    centre_x_matrix = numpy.array(centre_x)
    
    x_bar_matrix = numpy.dot(actual_noise_matrix, centre_x_matrix.T)
    print(x_bar_matrix)
    
    for c in range(len(x_bar_matrix)):
        for d in range(len(x_bar_matrix[c])):
            x_bar_matrix[c][d] = x_bar_matrix[c][d] / math.sqrt(N)
    print(x_bar_matrix)
    
    u, s, vh = numpy.linalg.svd(x_bar_matrix, full_matrices = True)
    print(u)
    print(s)
    print(vh)
    
    H = 0
    
    for q in s:
        if q > 1:
            H = H + 1
    
    print()
    print("S")
    print(s)
    print()
    
    l_H = []
    l_not_H = []
    
    for j1 in range(H):
        l_H.append(s[j1])
    for j2 in range(H, noise_length):
        l_not_H.append(s[j2])
    
    print(l_H)
    print(l_not_H)
    
    #H = 3
    
    """
    for j in range(len(vh)):
        for k in range(len(vh[j])):
            vh[j][k] = (vh[j][k])**2
    print()
    print(vh)
    H = len(vh)
    """
    
    A_H = []
    for g in range(H):
        temp = []
        for h in range(H):
            if g == h:
                temp.append(s[g] ** 2)
            else:
                temp.append(0)
        A_H.append(temp)
    print()
    print(A_H)
    A_H_matrix = numpy.array(A_H)
    
    
    
    
    U_H = []
    for i in range(len(u)):
        temp = []
        for j in range(H):
            temp.append(u[i][j])
        U_H.append(temp)
    print()
    print("HERE")
    print(U_H)
    U_H_matrix = numpy.array(U_H)
    
    I_H = []
    for r1 in range(H):
        temp = []
        for r2 in range(H):
            if r1 == r2:
                temp.append(1)
            else:
                temp.append(0)
        I_H.append(temp)
    I_H_matrix = numpy.array(I_H)
    print(I_H)
    
    
    
    
    
    
    new_new_noise_matrix = []
    for a in range(len(noise_matrix)):
        temp = []
        for b in range(len(noise_matrix[a])):
            if a == b:
                temp.append(math.sqrt(noise_matrix[a][b]))
            else:
                temp.append(0)
        new_new_noise_matrix.append(temp)
    print(new_new_noise_matrix)
    actual_new_new_noise_matrix = numpy.array(new_new_noise_matrix)
    
    F_1 = numpy.dot(actual_new_new_noise_matrix, U_H_matrix)
    print()
    print("F1")
    print(F_1)
    
    #F_2 = A_H_matrix
    F_2 = numpy.subtract(A_H_matrix, I_H_matrix)
    print()
    print("F2")
    print(F_2)
    for y1 in range(len(F_2)):
        for y2 in range(len(F_2[y1])):
            F_2[y1][y2] = math.sqrt(F_2[y1][y2])
            #F_2[y1][y2] = math.sqrt(abs(F_2[y1][y2] - 1))
            """
            if F_2[y1][y2] > 1:
                F_2[y1][y2] = math.sqrt(F_2[y1][y2] - 1)
            else:
                F_2[y1][y2] = math.sqrt(F_2[y1][y2])
            """
    print(F_2)
    F = numpy.dot(F_1, F_2)
    print(F)
    
    
    noise_2 = numpy.dot(F, F.T)
    print(noise_2)
    diagonal_2 = []
    for e1 in range(len(noise_2)):
        for e2 in range(len(noise_2[e1])):
            if e1 == e2:
                diagonal_2.append(noise_2[e1][e2])
    print()
    print("Diagonal_2")
    print(diagonal_2)
    
    diagonal_1 = variance
    print()
    print("Diagonal_1")
    print(diagonal_1)
    
    diagonal = []
    for w in range(len(diagonal_1)):
        diagonal.append(abs(diagonal_1[w] - diagonal_2[w]))
    print(diagonal)
    
    
    
    
    
    
    likelihood_left_1 = 0
    for v1 in range(H):
        likelihood_left_1 = likelihood_left_1 + math.log(l_H[v1])
    likelihood_left_2 = 0
    for v2 in range(noise_length - H):
        likelihood_left_1 = likelihood_left_1 + l_not_H[v2]
    likelihood_left = likelihood_left_1 + H + likelihood_left_2
    
    Pi_H = []
    for k1 in range(noise_length):
        temp = []
        for k2 in range(noise_length):
            if k1 == k2:
                temp.append(2 * math.pi)
            else:
                temp.append(0)
        Pi_H.append(temp)
    Pi_H_matrix = numpy.array(Pi_H)
    print(Pi_H_matrix)
    
    likelihood_right = math.log(numpy.linalg.det(numpy.multiply(Pi_H_matrix, noise_matrix)))
    
    likelihood = -N/2 * (likelihood_left + likelihood_right)
    
    print(likelihood)
    
    if abs(likelihood - previous_likelihood) < convergence_criteria:
        converge = True
    
    for t1 in range(noise_length):
        temp = []
        for t2 in range(noise_length):
            if t1 == t2:
                noise_matrix[t1][t2] = diagonal[t1]
            
    