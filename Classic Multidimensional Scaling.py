# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:00:54 2020

@author: Grant
"""

import numpy
import scipy.linalg as la

d = [[0, 1, 1, 2**(1/2)], [1, 0, 2**(1/2), 1], [1, 2**(1/2), 0, 1], [2**(1/2), 1, 1, 0]]

n = 4

D = []
for i in range(len(d)):
    temp = []
    for j in range (len(d[i])):
        temp.append(int((d[i][j])**2))
    D.append(temp)

matrix_D = numpy.array(D)

I_1 = [[1/n, 1/n, 1/n, 1/n], [1/n, 1/n, 1/n, 1/n], [1/n, 1/n, 1/n, 1/n], [1/n, 1/n, 1/n, 1/n]]
I = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
matrix_I_1 = numpy.array(I_1)
matrix_I = numpy.array(I)
J = numpy.subtract(matrix_I, matrix_I_1)

B = numpy.dot(numpy.dot(J[:], D[:]), J[:])

for a in range(len(B)):
    for b in range(len(B[a])):
        B[a][b] = -1/2 * B[a][b]

e_vals, e_vecs = numpy.linalg.eig(B)

for i in range(len(e_vals)):
    if abs(e_vals[i] - int(e_vals[i])) < 0.01:
        e_vals[i] = int(e_vals[i])

d = 2
count = 0
rows = 0

lam = []
count_matrix = []
while count < n and rows < 2:
    if e_vals[count] != 0:
        temp = []
        for i in range(d):
            if i == rows:
                temp.append((e_vals[count])**(1/2))
            else:
                temp.append(0)
        lam.append(temp)
        count_matrix.append(count)
        rows += 1
    count += 1

v = []
for x in count_matrix:
    row = n - 1 - x
    v.append(e_vecs[row])

matrix_lam = numpy.array(lam)
matrix_v = numpy.array(v)

print(numpy.dot(matrix_lam, matrix_v))





        
        