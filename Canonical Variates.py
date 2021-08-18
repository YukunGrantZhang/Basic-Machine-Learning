# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:50:36 2020

@author: Grant
"""

import numpy

import scipy.linalg

data = [[[1, 2], 0], [[2, 3], 0], [[1, 3], 0], [[3, 5], 0], [[8, 1], 1], [[8, 3], 1], [[9, 1], 1]]

#mean of whole dataset
mx = 0
my = 0
for d in data:
    mx = mx + d[0][0]
mx = mx / len(data)

for da in data:
    my = my + d[0][1]
my = my / len(data)

m = [mx, my]
print(m)




#mean of each class
mc = []
classes_n = []
classes = 2
for c in range(classes):
    mcx = 0
    mcy = 0
    count_class = 0
    
    for e in data:
        if e[1] == c:
            count_class = count_class + 1 
            mcx = mcx + e[0][0]
    mcx = mcx / count_class
    
    for ea in data:
        if ea[1] == c:
            mcy = mcy + ea[0][1]
    mcy = mcy / count_class
    
    classes_n.append(count_class)
    
    mc.append([mcx, mcy])

print(mc)
print(classes_n)

mc_m = []

for a in mc:
    x = a[0] - m[0]
    y = a[1] - m[1]
    
    mc_m.append([x, y])
print(mc_m)




#Compute A
mc_m_0 = [mc_m[0]]

mc_0_matrix = numpy.array(mc_m_0)
print(mc_0_matrix)

mc_0_matrix_T = mc_0_matrix.T
print(mc_0_matrix_T)

mc_0_product = numpy.dot(mc_0_matrix_T, mc_0_matrix)
Nc_0 = numpy.array([[classes_n[0], classes_n[0]], [classes_n[0], classes_n[0]]])
mc_0_product = numpy.multiply(mc_0_product, Nc_0)
print(mc_0_product)
print()

mc_m_1 = [mc_m[1]]

mc_1_matrix = numpy.array(mc_m_1)
print(mc_1_matrix)

mc_1_matrix_T = mc_1_matrix.T
print(mc_1_matrix_T)

mc_1_product = numpy.dot(mc_1_matrix_T, mc_1_matrix)
Nc_1 = numpy.array([[classes_n[1], classes_n[1]], [classes_n[1], classes_n[1]]])
mc_1_product = numpy.multiply(mc_1_product, Nc_1)
print(mc_1_product)
print()

A = numpy.add(mc_0_product, mc_1_product)
print(A)
print()



#Compute B
matrix = []

for ce in range(classes):
    temp_x = []
    temp_y = []
    for r in data:
        if r[1] == ce:
            temp_x.append(r[0][0])
            temp_y.append(r[0][1])
    matrix.append([temp_x, temp_y])

print(matrix)

covariance_0 = numpy.array(matrix[0])

covariance_0_matrix = numpy.cov(covariance_0, bias=True)
covariance_0_matrix = numpy.multiply(covariance_0_matrix, Nc_0)
print(covariance_0_matrix)
    
covariance_1 = numpy.array(matrix[1])

covariance_1_matrix = numpy.cov(covariance_1, bias=True)
covariance_1_matrix = numpy.multiply(covariance_1_matrix, Nc_1)
print(covariance_1_matrix)

B = numpy.add(covariance_0_matrix, covariance_1_matrix)
print(B)
print()

#Computer Cholesky factor
L = scipy.linalg.cholesky(B, lower=True)
print(L)
print()


#Compute B-TAB-1
BT = L.T
#print(BT)
B_T = numpy.linalg.inv(BT)
print(B_T)

#Compute B-1
B_1 = numpy.linalg.inv(L)
print(B_1)

multiple = numpy.dot(numpy.dot(B_T, A), B_1)
print(multiple)
print()

#find eigenvectors
w, v = numpy.linalg.eig(multiple)
print(w)
print(v)
print()



#final point projections
points = []
for u in data:
    points.append(u[0])
print(points)

projected_points = []
for y in points:
    projected_points.append(numpy.dot(y, v.T))
print(projected_points)