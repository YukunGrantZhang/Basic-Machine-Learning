# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:24:46 2020

@author: Grant
"""

import math

training_data = [[1, 5], [2, 8], [3, 6], [4, 5], [4, 4], [5, 6]]
C = 8
n = len(training_data)

x_y = []
for a in range(n):
    x_y.append(training_data[a][0] * training_data[a][1])

def gaussian_kernel(x_i, x_j, sigma):
    answer = math.exp(-(abs(x_i - x_j))**2 / (2 * sigma**2))
    
    return answer

alphas = [0, 0, 0, 0, 0, 0]
previous_total = -100000000000000

result = []
temp_alphas = []

for a1 in range(0, int(C/n*10), 2):
    a1 = a1 / 10
    for a2 in range(0, int(C/n*10), 2):
        a2 = a2 / 10
        for a3 in range(0, int(C/n*10), 2):
            a3 = a3 / 10
            for a4 in range(0, int(C/n*10), 2):
                a4 = a4 / 10
                for a5 in range(0, int(C/n*10), 2):
                    a5 = a5 / 10
                    for a6 in range(0, int(C/n*10), 2):
                        a6 = a6 / 10
                
                        sum_1 = a1 + a2 + a3 + a4 + a5 + a6
                
                        temp_alphas.clear()
                        temp_alphas = [a1, a2, a3, a4, a5, a6]
                
                        sum_2 = 0
                
                        for i in range(len(training_data)):
                            for j in range(len(training_data)):
                                sum_2 += (temp_alphas[i] * temp_alphas[j] * training_data[i][1] * training_data[j][1] * gaussian_kernel(training_data[i][0], training_data[j][0], 1))
                    
                        sum_2 = sum_2 / 2
                
                        total = sum_1 - sum_2
                
                        result.append([a1, a2, a3, a4, a5, a6, total])
                
result.sort(key=lambda x:x[6], reverse = True)

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