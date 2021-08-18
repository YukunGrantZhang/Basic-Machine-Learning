# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:25:25 2020

@author: Grant
"""

X = [[1, 3, 5], [2, 6, 8], [3, 1, 6]]
Y = [45, 78, 56]
    
set_l1 = 0
set_l2 = 0
set_l3 = 0

breaking = 0

number_of_variables = 3

low_values = []
for l1 in range(0, 200, 2):
    l1 = l1 / 10
    for l2 in range(0, 200, 2):
        l2 = l2 / 10
        for l3 in range(0, 200, 2):
            l3 = l3 / 10
            temp_sum = 0
            
            for a in range(number_of_variables):
                temp_sum += abs(Y[a] - l1*X[a][0] - l2*X[a][1] - l3*X[a][2])

            if abs(temp_sum) <= 0.5:
                set_l1 = l1
                set_l2 = l2
                set_l3 = l3
                breaking = 1
                break
            
            if breaking == 1:
                break
        if breaking == 1:
            break
    if breaking == 1:
        break
        
print(f"The lasso coefficients for l1 is {set_l1}, l2 is {set_l2}, l3 is {set_l3}")