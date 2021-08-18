# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:40:42 2020

@author: Grant
"""

training_data = [[[0, 1]], [[1, 1]], [[2, 2]], [[2, 1]], [[1, 2]], [[5, 5]], [[5, 6]], [[6, 6]], [[6, 7]], [[3, 11]], [[4, 12]], [[3, 12]]]

def distance(set_1, set_2):
    distance_matrix = []
    for s1 in set_1:
        for s2 in set_2:
            temp = []
            d = ((s1[0] - s2[0])**2 + (s1[1] - s2[1])**2)**(1/2)
            temp.append(s1)
            temp.append(s2)
            temp.append(d)
            distance_matrix.append(temp)
    distance_matrix.sort(key=lambda x: x[2])
    return distance_matrix[0][2]

dendogram = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]

while len(training_data) > 1:
    single_linkage_matrix = []
    for i in range(len(training_data)):
        for j in range(len(training_data)):
            if i == j:
                continue
            
            temp = []
            d = distance(training_data[i], training_data[j])
            temp.append(i)
            temp.append(j)
            temp.append(d)
            
            single_linkage_matrix.append(temp)
    
    single_linkage_matrix.sort(key = lambda x: x[2])
    
    chosen_point_i = single_linkage_matrix[0][0]
    chosen_point_j = single_linkage_matrix[0][1]
    
    dendogram[chosen_point_i].append(dendogram[chosen_point_j])
    dendogram.pop(chosen_point_j)
    
    for x in range(len(training_data[chosen_point_j])):
        element = training_data[chosen_point_j][x]
        training_data[chosen_point_i].append(element)
    
    training_data.pop(chosen_point_j)
    n += 1

print(dendogram)
    
    
    
            
            