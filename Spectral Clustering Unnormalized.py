# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:38:24 2020

@author: Grant
"""

import numpy
import random

W = [[0, 2, 1, 0, 0, 0, 0, 0], [2, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 3, 0]]
D = [[3, 0, 0, 0, 0, 0, 0, 0], [0, 3, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 3, 0], [0, 0, 0, 0, 0, 0, 0, 3]]

print(W)
print(D)

L = numpy.subtract(D, W)

print(L)

eig_vals, eig_vecs = numpy.linalg.eig(L)

print(eig_vals)
print(eig_vecs)

classification = []
for e in range(len(eig_vals)):
    temp = []
    temp.append(e)
    temp.append(eig_vals[e])
    classification.append(temp)
classification.sort(key = lambda x: x[1])
print(classification)

clusters = 3
clusters_location = []
for a in range(clusters):
    clusters_location.append(classification[a][0])
clusters_location.sort()
print(clusters_location)


V = []
n = 8
for i in range(n):
    temp = []
    for x in clusters_location:
        temp.append(eig_vecs[x][i])
    V.append(temp)
print(V)

for a in V:
    a.append(0)

print(V)

number_of_clusters = 3

centres = []
point_chosen = random.randint(0, len(V))
temp = []
temp.append(V[point_chosen][0])
temp.append(V[point_chosen][1])
temp.append(V[point_chosen][2])
centres.append(temp)

while len(centres) < number_of_clusters:
    temp_clusters = []
    for p in range(len(V)):
        if [V[p][0], V[p][1], V[p][2]] in centres:
            continue
        temp_distances = []
        for i in range(len(centres)):
            t = []
            d = ((centres[i][0] - V[p][0])**2 + (centres[i][1] - V[p][1])**2 + (centres[i][2] - V[p][2])**2)**(1/2)
            t.append(p)
            t.append(d)
            temp_distances.append(t)
        temp_distances.sort(key = lambda x: x[1])
        temp_clusters.append(temp_distances[0])
    temp_clusters.sort(key = lambda x: x[1], reverse=True)
    temp = []
    temp.append(V[temp_clusters[0][0]][0])
    temp.append(V[temp_clusters[0][0]][1])
    temp.append(V[temp_clusters[0][0]][2])
    centres.append(temp)

n = 10
count = 0
while count < 10:
    for point in V:
        temp_centres = []
        for i in range(len(centres)):
            temp = []
            distance = ((centres[i][0] - point[0])**2 + (centres[i][1] - point[1])**2 + (centres[i][2] - point[2])**2)**(1/2)
            temp.append(i)
            temp.append(distance)
            temp_centres.append(temp)
        temp_centres.sort(key=lambda x: x[1])
        
        point[3] = temp_centres[0][0]
    
    for j in range(len(centres)):
        summation_x = 0
        count_x = 0
        summation_y = 0
        count_y = 0
        summation_z = 0
        count_z = 0
        for k in V:
            if k[3] == j:
                summation_x += k[0]
                count_x += 1
                summation_y += k[1]
                count_y += 1
                summation_z += k[1]
                count_z += 1
        centres[i][0] = summation_x / count_x
        centres[i][1] = summation_y / count_y
        centres[i][2] = summation_z / count_z
    
    count += 1
print(V)
    
