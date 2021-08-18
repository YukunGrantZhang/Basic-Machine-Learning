# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:12:41 2020

@author: Grant
"""

import random

training_data = [[0, 1, 0], [1, 1, 0], [2, 2, 0], [2, 1, 0], [1, 2, 0], [5, 5, 0], [5, 6, 0], [6, 6, 0], [6, 7, 0], [3, 11, 0], [4, 12, 0], [3, 12, 0]]

number_of_clusters = 3

centres = []
point_chosen = random.randint(0, len(training_data))
temp = []
temp.append(training_data[point_chosen][0])
temp.append(training_data[point_chosen][1])
centres.append(temp)

while len(centres) < number_of_clusters:
    temp_clusters = []
    for p in range(len(training_data)):
        if [training_data[p][0], training_data[p][1]] in centres:
            continue
        temp_distances = []
        for i in range(len(centres)):
            t = []
            d = ((centres[i][0] - training_data[p][0])**2 + (centres[i][1] - training_data[p][1])**2)**(1/2)
            t.append(p)
            t.append(d)
            temp_distances.append(t)
        temp_distances.sort(key = lambda x: x[1])
        temp_clusters.append(temp_distances[0])
    temp_clusters.sort(key = lambda x: x[1], reverse=True)
    temp = []
    temp.append(training_data[temp_clusters[0][0]][0])
    temp.append(training_data[temp_clusters[0][0]][1])
    centres.append(temp)

n = 10
count = 0
while count < 10:
    for point in training_data:
        temp_centres = []
        for i in range(len(centres)):
            temp = []
            distance = ((centres[i][0] - point[0])**2 + (centres[i][1] - point[1])**2)**(1/2)
            temp.append(i)
            temp.append(distance)
            temp_centres.append(temp)
        temp_centres.sort(key=lambda x: x[1])
        
        point[2] = temp_centres[0][0]
    
    for j in range(len(centres)):
        summation_x = 0
        count_x = 0
        summation_y = 0
        count_y = 0
        for k in training_data:
            if k[2] == j:
                summation_x += k[0]
                count_x += 1
                summation_y += k[1]
                count_y += 1
        centres[i][0] = summation_x / count_x
        centres[i][1] = summation_y / count_y
    
    count += 1
print(training_data)
