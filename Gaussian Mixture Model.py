# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:02:27 2020

@author: Grant
"""

import numpy

import math

data = [[1, 2], [1, 1], [2, 1], [8, 1], [8, 2], [9, 1]]

N = len(data)
H = 2

m = [[1, 3], [6, 2]]

p = [0.4, 0.6]

s = []
x_m = []
for i in range(len(m)):
    x_m = []
    for n in range(len(data)):
        temp_x = data[n][0] - m[i][0]
        temp_y = data[n][1] - m[i][1]
        x_m.append([temp_x, temp_y])
    x_m_matrix = numpy.array(x_m)
    
    s_m = numpy.dot(x_m_matrix.T, x_m_matrix)
    
    print(s_m)
    
    length = len(s_m)

    p_m = [[p[i]] * length] * length
    
    p_matrix = numpy.array(p_m)
    
    print(p_matrix)
    
    s_matrix = numpy.multiply(p_matrix, s_m)
    
    print(s_matrix)
    
    temp_1 = []
    for a in range(len(s_matrix)):
        temp_2 = []
        for b in range(len(s_matrix[a])):
            temp_2.append(s_matrix[a][b])
        temp_1.append(temp_2)
    s.append(temp_1[:])

print()
print("HERE")
print(s)
print("HERE")

convergence_criteria = 0.1

solution = 0.3

v = 0

converge = False
while converge == False or v < 150:
    
    previous_solution = solution
    
    p_n_i = []
    
    for n in range(N):
        p_i_x = []
        for i in range(H):
            s_i = numpy.matrix(s[i])
            
            x_m = []
            temp_x = data[n][0] - m[i][0]
            temp_y = data[n][1] - m[i][1]
            x_m.append([temp_x, temp_y])
            x_m_matrix = numpy.array(x_m)
            
            length = len(s_i)
            p_i = [[p[i]] * length] * length
            p_i_matrix = numpy.array(p_m)
            
            part_1 = numpy.dot(x_m_matrix, numpy.linalg.inv(s_i))
            #print(part_1)
            temp = numpy.dot(part_1, x_m_matrix.T)
            #print(temp)
            
            d = numpy.linalg.det(s_i)
            #print(d)
            
            t = temp[0][0]
            #print(t)
            
            answer = p[i] * math.exp(-1/2 * temp[0][0]) * (d**(-1/2))
            #print("HERE")
            #print(answer)
            p_i_x.append(answer)
        
        #print()
        #print("HERE")
        #print(p_i_x)
        
        p_i_x_normalise = []
        summation = 0
        for e in p_i_x:
            summation = summation + e
        for g in p_i_x:
            p_i_x_normalise.append(g / summation)
        
        p_n_i.append(p_i_x_normalise)
    
    print(p_n_i)
    print()
    
    p_n_i_normalise = p_n_i[:]
    
    for a in range(H):
        summation = 0
        for n in p_n_i:
            summation = summation + n[a]
        
        for q in p_n_i_normalise:
            q[a] = q[a] / summation
            
    print(p_n_i_normalise)        
    
    for i in range(H):
        temp_x_i = 0
        temp_y_i = 0
        for n in range(N):
            temp_x = p_n_i_normalise[n][i] * data[n][0]
            temp_y = p_n_i_normalise[n][i] * data[n][1]
            
            temp_x_i = temp_x_i + temp_x
            temp_y_i = temp_y_i + temp_y
        
        m[i][0] = temp_x_i
        m[i][1] = temp_y_i
    
    print(m)
    print()
    
    s = []
    x_m = []
    for i in range(H):
        x_m = []
        for n in range(N):
            temp_x = data[n][0] - m[i][0]
            temp_y = data[n][1] - m[i][1]
            
            pni = p_n_i_normalise[n][i]
            
            x_m.append([pni * temp_x, pni * temp_y])
        x_m_matrix = numpy.array(x_m)
        
        print(x_m_matrix)
        
        s_m = numpy.dot(x_m_matrix.T, x_m_matrix)
    
        print(s_m)
        
        s_matrix = numpy.array(s_m)
    
        print(s_matrix)
    
        temp_1 = []
        for a in range(len(s_matrix)):
            temp_2 = []
            for b in range(len(s_matrix[a])):
                temp_2.append(s_matrix[a][b])
            temp_1.append(temp_2)
        s.append(temp_1[:])
    
    print()
    print(s)
    
    for i in range(H):
        summation = 0
        
        for n in range(N):
            summation = summation + p_n_i[n][i]
        
        p[i] = summation / N
    
    print()
    print(p)
    
    solution = 0
    
    for n in range(N):
        temp_solution = 0
        for i in range(H):
            s_i = numpy.matrix(s[i])
            
            x_m = []
            temp_x = data[n][0] - m[i][0]
            temp_y = data[n][1] - m[i][1]
            x_m.append([temp_x, temp_y])
            x_m_matrix = numpy.array(x_m)
            
            length = len(s_i)
            p_i = [[p[i]] * length] * length
            p_i_matrix = numpy.array(p_m)
            
            part_1 = numpy.dot(x_m_matrix, numpy.linalg.inv(s_i))
            
            temp = numpy.dot(part_1, x_m_matrix.T)
            print("HERE")
            print(temp)
            
            pi2 = [[2*math.pi] * length] * length
            pi2_matrix = numpy.array(pi2)
            
            pi2Si = numpy.multiply(pi2_matrix, s_i)
            
            d = numpy.linalg.det(pi2Si)
            print(d)
            
            t = temp[0][0]
            
            answer = p[i] * math.exp(-1/2 * temp[0][0]) * (d**(-1/2))
            
            temp_solution = temp_solution + answer
        
        temp_solution = math.log(temp_solution)
        
        solution = solution + temp_solution
    
    if solution - previous_solution < convergence_criteria:
        converge = True
    
    v = v + 1

print(m)
