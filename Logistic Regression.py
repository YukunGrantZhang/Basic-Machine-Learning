# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:29:16 2020

@author: Grant
"""

import math

training_data = [[1, 7], [2, 6], [1, 5], [5, 1], [6, 1], [7, 2]]
lam = 0.3

def classify(x, y, w, b):
    result = w*x + b
    if result >= y:
        return 1
    else:
        return -1

results = []
for b in range(-200, 200, 1):
    b = b / 10
    for w in range(-100, 100, 1):
        w = w / 10
        temp_sum_1 = 0
        temp_sum_2 = 0
        
        temp_result = []
        for a in training_data:
            x = a[0]
            y = a[1]
            
            temp_sum_1 += math.log2(1 + math.exp(-(classify(x, y, w, b))*(y - w*x - b)))
        
        temp_sum_1 = temp_sum_1 / len(training_data)
        temp_sum_2 = lam * abs(w)
        temp_sum = temp_sum_1 + temp_sum_2
        
        temp_result.append(w)
        temp_result.append(b)
        temp_result.append(temp_sum)
        
        print(temp_result)
        
        results.append(temp_result)

results.sort(key = lambda x: x[2])

print(f"The ideal separation classification line is y={results[0][0]}x + {results[0][1]}")