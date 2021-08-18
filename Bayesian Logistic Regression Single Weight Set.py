# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:02:52 2020

@author: Grant
"""

import numpy

import math

#simplistic example with n = 1
data = [[1, 3], [2, 4], [3, 5], [4, 3], [5, 8], [6, 3], [8, 1]]

B = 7

alpha = 0.1

w = [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]

#spread c out evenly between 1 to 8
c = [1.875, 2.75, 3.625, 4.5, 5.375, 6.25, 7.125]
l = 0.3

converge = False
convergence_criteria = 0.1

while converge == False:
    
    previous_alpha = 0.1
    
    w_converge = False
    
    while w_converge == False:
        w_previous = w[:]
        #calculate phi_n and hn
        phi_n = []
        for d in range(len(data)):
            phi_n.append(math.exp(-0.5*(data[d][0] - c[d])**2 / l**2))
    
        print(phi_n)
        print()
        matrix_phi_n = numpy.array([phi_n])
        print(matrix_phi_n)
    
        hn = []
        for p in range(len(phi_n)):
            hn.append((2*c[p] - 1)*phi_n[p])
        print("HERE")
        print(hn)
    
        matrix_w = numpy.array(w)
        matrix_hn = numpy.array(hn)
    
        product = numpy.dot(matrix_w, matrix_hn)
        sigma = 1 / (1 + math.exp(-product))
        print(sigma)
    
        #find h
        dphi = numpy.dot(matrix_phi_n.T, matrix_phi_n)
        matrix_sigma = numpy.array([[sigma*(1-sigma)] * len(phi_n)] * len(phi_n))
        h_right = numpy.multiply(matrix_sigma, dphi)
        print(h_right)
    
        aI = [[alpha] * len(phi_n)] * len(phi_n)
        matrix_aI = numpy.array(aI)
    
        h = numpy.add(matrix_aI, h_right)
        print(h)
        print()
    
        #find delta e
        delta_e_left = []
        for a in w:
            delta_e_left.append(alpha * a)
        print(delta_e_left)
    
        delta_e_right = []
        for b in hn:
            delta_e_right.append((1-sigma) * b)
        print(delta_e_right)
    
        delta_e = []
        for a in range(len(delta_e_left)):
            delta_e.append(delta_e_left[a] - delta_e_right[a])
        print(delta_e)
        matrix_delta_e = numpy.array(delta_e)
        print()
        print()
        print()
    
        #calculate new w
        w_new_left = numpy.array(w)
        print(w_new_left)
    
        w_new_right = numpy.dot(numpy.linalg.pinv(h), matrix_delta_e)
        print(w_new_right)
    
        w_new = numpy.subtract(w_new_left, w_new_right)
        print(w_new)
    
        w_update = []
        for i in range(len(w_new)):
            w_update.append(w_new[i])
        print(w_update)
    
        w = w_update[:]
    
        w_converge = True
        for j in range(len(w)):
            difference = w[j] - w_previous[j]
            if difference > convergence_criteria:
                w_converge = False
    
    print("HERE")
    print(w)
    
    temp_x = []
    temp_y = []
    for d in data:
        temp_x.append(d[0])
        temp_y.append(d[1])
    temp = [temp_x, temp_y]
    print(temp)
    S = numpy.cov(temp, bias=True)
    print(S)
    
    trace = 0
    for a in range(len(S)):
        for b in range(len(S[a])):
            if a == b:
                trace = trace + S[a][b]
    print(trace)
    
    mean_x = 0
    mean_y = 0
    for d in data:
        mean_x = mean_x + d[0]
        mean_y = mean_y + d[1]
    mean_x = mean_x / len(data)
    mean_y = mean_y / len(data)
    
    m = [mean_x, mean_y]
    matrix_m = numpy.array(m)
    
    mean = numpy.dot(matrix_m, matrix_m.T)
    print(mean)
    
    alpha = B / (trace + mean)
    print(alpha)
    
    converge = True    
    if alpha - previous_alpha > convergence_criteria:
        converge = False