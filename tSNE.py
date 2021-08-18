# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:57:11 2020

@author: Grant
"""

import math

training_data = [[1, 3], [2, 4], [1, 5], [5, 1], [6, 2], [8, 1]]
sigmas = [3, 3, 3, 2, 2, 2]

dij = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

for i in range(len(training_data)):
    for j in range(len(training_data)):
        dij[i][j] = ((training_data[i][0] - training_data[j][0])**2 + (training_data[i][1] - training_data[j][1])**2)**(1/2)

tpij = [0, 0, 0, 0, 0, 0]
for a in range(len(tpij)):
    total = 0
    
    for b in range(len(dij[a])):
        total += math.exp((dij[a][b])/(2*(sigmas[a])**2))

    tpij[a] = total

pij = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
for i in range(len(dij)):
    for j in range(len(dij)):
        s = sigmas[i]
        d = dij[i][j]
        t = tpij[i]
        
        pij[i][j] = math.exp(d/(2 * s**2))/t

qij = pij[:]

def tune(x, y, learning_rate):
    global pij
    global qij
    
    q_deriv = 0
    N = len(qij)
    
    total = 0
    for a in range(N):
        total += (1 + (qij[x][a]))**(-1)
    
    for i in range(N):
        for j in range(N):
            q_deriv += -pij[i][j] / (((1 + (qij[x][y]))**(-1)) / total)
    
    qij[x][y] -=  (q_deriv / float(N**2)) * learning_rate
    qij[y][x] = qij[x][y]

def tsne(learning_rate):
    for a in range(len(qij)):
        for b in range(len(qij)):
            tune(a, b, learning_rate)

    print(qij)

tsne(0.1)
        
        
        
        

