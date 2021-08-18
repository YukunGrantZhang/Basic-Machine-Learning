# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:46:11 2020

@author: Grant
"""

training_data = [[1, 7], [2, 6], [1, 5], [5, 1], [6, 1], [7, 2]]

results = []
for b in range(-200, 200, 1):
    b = b / 10
    for w in range(-100, 100, 1):
        w = w / 10
        temp_sum = 0;
        
        temp_result = []
        for a in training_data:
            x = a[0]
            y = a[1]
            
            temp_sum += (y - w*x - b)**2
        
        temp_result.append(w)
        temp_result.append(b)
        temp_result.append(temp_sum)
        
        print(temp_result)
        
        results.append(temp_result)

results.sort(key = lambda x: x[2])

print(f"The ideal separation classification line is y={results[0][0]}x + {results[0][1]}")
        