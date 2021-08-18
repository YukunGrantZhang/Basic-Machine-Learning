# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:13:59 2020

@author: Grant
"""

training_set = [[5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [21, 0], [33, 0], [25, 0], [35, 0]]

test_set = [[3], [21], [55]]

k = 5

distances = []
temp_set = training_set[:]
for a in test_set:
    distances.clear()
    current_value = a[0]
    
    for b in temp_set:
        d = abs(b[0] - current_value)
        label = b[1]
        distances.append([d, label])
    
    distances.sort(key=lambda tup: tup[0])
    
    #print(distances)
    
    sum_values = 0
    for c in range(0, k):
        sum_values += distances[c][1]
    
    if sum_values <= k/2:
        a.append(0)
    else:
        a.append(1)

print(test_set)
        