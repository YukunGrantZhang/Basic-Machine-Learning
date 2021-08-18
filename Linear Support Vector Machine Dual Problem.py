# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:11:58 2020

@author: Grant
"""

import math

training_data = [[1, 7], [2, 6], [5, 1], [6, 1]]
C = 11
n = len(training_data)

x_y = []
for a in range(n):
    x_y.append(training_data[a][0] * training_data[a][1])

alphas = [0, 0, 0, 0, 0, 0]
previous_total = -100000000000000

result = []
temp_alphas = []

for a1 in range(0, int(C/n*10)):
    a1 = a1 / 10
    for a2 in range(0, int(C/n*10)):
        a2 = a2 / 10
        for a3 in range(0, int(C/n*10)):
            a3 = a3 / 10
            for a4 in range(0, int(C/n*10)):
                a4 = a4 / 10
                
                sum_1 = a1 + a2 + a3 + a4
                
                temp_alphas.clear()
                temp_alphas = [a1, a2, a3, a4]
                
                sum_2 = 0
                
                for i in range(len(training_data)):
                    for j in range(len(training_data)):
                        sum_2 += (temp_alphas[i] * temp_alphas[j] * training_data[i][0] * training_data[j][0] * training_data[i][1] * training_data[j][1])
                    
                sum_2 = sum_2 / 2
                
                total = sum_1 - sum_2
                
                result.append([a1, a2, a3, a4, total])
                
result.sort(key=lambda x:x[4], reverse = True)

w = 0
for a in range(len(x_y)):
    w += result[1][a] * x_y[a]

b = 0
for j in range (len(x_y)):
    sum_1 = training_data[j][1]
    sum_2 = 0
    for i in range(len(x_y)):
        sum_2 += result[1][i] * x_y[i] * training_data[j][0]
    
    temp_sum = sum_1 - sum_2
    
    b += (temp_sum / (len(training_data))) 

print(f"The line is y = {w}x + {b}")
