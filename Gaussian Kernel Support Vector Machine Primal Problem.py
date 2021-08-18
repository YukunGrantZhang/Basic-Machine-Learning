# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:02:30 2020

@author: Grant
"""

import math

training_data = [[1, 5], [2, 8], [3, 6], [4, 5], [4, 4], [5, 6]]
C = 8
n = len(training_data)

x_y = []
for a in range(n):
    x_y.append(training_data[a][0] * training_data[a][1])

def classify(x, y, w, b):
    result = w*x + b
    if result >= y:
        return 1
    else:
        return -1

def maximiser(x, y, w, b):
    choice_1 = 0
    middle = (classify(x, y, w, b))*(y - w*x - b)
    choice_2 = 1 - middle
    
    return max(choice_1, choice_2)

def gaussian_kernel(x_i, x_j, sigma):
    answer = math.exp(-(abs(x_i - x_j))**2 / (2 * sigma**2))
    
    return answer

alphas = [0, 0, 0, 0, 0, 0]
previous_total = -100000000000000

result = []
temp_betas = []

for b1 in range(0, int(C/n*10), 3):
    b1 = b1 / 10
    for b2 in range(0, int(C/n*10), 3):
        b2 = b2 / 10
        for b3 in range(0, int(C/n*10), 3):
            b3 = b3 / 10
            for b4 in range(0, int(C/n*10), 3):
                b4 = b4 / 10
                for b5 in range(0, int(C/n*10), 3):
                    b5 = b5 / 10
                    for b6 in range(0, int(C/n*10), 3):
                        b6 = b6 / 10
                        for b in range(-200, 200, 5):
                            b = b / 10
                
                            #sum_1 = b1 + b2 + b3 + b4 + b5 + b6
                
                            temp_betas.clear()
                            temp_betas = [b1, b2, b3, b4, b5, b6]
                
                            sum_1 = 0
                
                            for i in range(len(training_data)):
                                for j in range(len(training_data)):
                                    sum_1 += (temp_betas[i] * temp_betas[j] * gaussian_kernel(training_data[i][0], training_data[j][0], 1))
                    
                            sum_1 = sum_1 / 2
                        
                            sum_2 = 0
                            part_1 = 0
                        
                            for i in range(len(training_data)):
                                part_1 = 0
                                x = training_data[i][0]
                                y = training_data[i][1]
                            
                                for j in range(len(training_data)):
                                    part_1 += temp_betas[j] * gaussian_kernel(training_data[i][0], training_data[j][0], 1)
                            
                                sum_2 += maximiser(x, y, part_1, b)
                        
                            sum_2 = C * sum_2 / n
                
                            total = sum_1 + sum_2
                
                            result.append([part_1, b, total])
                
result.sort(key=lambda x:x[2])

w = result[0][0]

b = result[0][1]

print(f"The line is y = {w}x + {b}")