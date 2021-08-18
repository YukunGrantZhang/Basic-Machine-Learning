# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:32:57 2020

@author: Grant
"""

import numpy
import itertools

W1 = [[0, 2, 0, 1, 0, 0, 0, 0], [2, 0, 5, 1, 3, 0, 0, 0], [0, 5, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 3, 1, 0, 0], [0, 3, 1, 3, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 3], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 3, 1, 0]]
D1 = [[3, 0, 0, 0, 0, 0, 0, 0], [0, 11, 0, 0, 0, 0, 0, 0], [0, 0, 6, 0, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 0, 0], [0, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 4]]
f1 = numpy.array([[1], [1], [1], [1], [1], [-1], [-1], [-1]])

W2 = [[0, 2, 1, 0, 0, 0, 0, 0], [2, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 3, 0]]
D2 = [[3, 0, 0, 0, 0, 0, 0, 0], [0, 3, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 3, 0], [0, 0, 0, 0, 0, 0, 0, 3]]
f2 = numpy.array([[1], [1], [1], [-1], [-1], [-1], [1], [1]])

W = W1
D = D1
f = f1

print(W)
print(D)

"""
Computing Standard Laplacian
"""

L = numpy.subtract(D, W)

print(L)

eig_vals, eig_vecs = numpy.linalg.eig(L)

for a in range(len(eig_vals)):
    if abs(int(eig_vals[a]) - eig_vals[a]) < 0.01:
        eig_vals[a] = int(eig_vals[a])

print(eig_vals)
print(eig_vecs)

value = numpy.dot(numpy.dot(f.T, L), f)
print(value)
print()

"""
Computing Symmetric Laplacian
"""

D_1_2 = []
for i in range(len(D)):
    temp = []
    for j in range(len(D[i])):
        if D[i][j] != 0:
            temp.append((D[i][j])**(-1/2))
        else:
            temp.append(0)
    D_1_2.append(temp)
print(D_1_2)
L_SYM = numpy.dot(numpy.dot(D_1_2, L), D_1_2)
print(L_SYM)

eig_vals_sym, eig_vecs_sym = numpy.linalg.eig(L_SYM)

for a in range(len(eig_vals_sym)):
    if abs(int(eig_vals_sym[a]) - eig_vals_sym[a]) < 0.01:
        eig_vals_sym[a] = int(eig_vals_sym[a])

print(eig_vals_sym)
print(eig_vecs_sym)

value_sym = numpy.dot(numpy.dot(f.T, L_SYM), f)
print(value_sym)
print()

"""
Computing Random Walk Laplacian
"""

L_RW = numpy.dot(numpy.linalg.inv(D), L)
print(L_RW)

eig_vals_rw, eig_vecs_rw = numpy.linalg.eig(L_RW)

for a in range(len(eig_vals_rw)):
    if abs(int(eig_vals_rw[a]) - eig_vals_rw[a]) < 0.01:
        eig_vals_rw[a] = int(eig_vals_rw[a])

print(eig_vals_rw)
print(eig_vecs_rw)

value_rw = numpy.dot(numpy.dot(f.T, L_RW), f)
print(value_rw)
print()

"""
Computer Cheeger Constants
"""
Sets = [0, 1, 2, 3, 4, 5, 6, 7]

h_min = []

for L in range(0, len(Sets)+1):
    for subset in itertools.combinations(Sets, L):
        new_Sets = Sets[:]
        
        temp = []
        for i in subset:
            temp.append(i)
        
        if temp == [] or temp == [0, 1, 2, 3, 4, 5, 6, 7]:
            continue
        
        for x in temp:
            new_Sets.remove(x)
        
        S = temp[:]
        S_C = new_Sets[:]

        vol_S = 0 
        for x in range(len(S)):
            vol_S += D[S[x]][S[x]]

        vol_S_C = 0 
        for x in range(len(S_C)):
            vol_S_C += D[S_C[x]][S_C[x]]

        cut_S = 0
        for i in range(len(S)):
            for j in range(len(S_C)):
                cut_S += W[S[i]][S_C[j]]

        h = cut_S / min(vol_S, vol_S_C)
        
        h_min.append(h)

h_min.sort()
print(h_min[0])