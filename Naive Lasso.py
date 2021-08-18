# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:19:37 2020

@author: Grant
"""

X = [[1, 3, 5], [2, 6, 8], [3, 1, 6]]
Y = [45, 78, 56]
    
def lasso(x, y, l1, l2, l3, lam, n):
    first_term = 0
    second_term = 0
    
    for a in range(n):
        first_term += (y[a] - l1*x[a][0] - l2*x[a][1] - l3*x[a][2])**2
    
    first_term = first_term / n
    second_term = lam * (l1 + l2 + l3)
    
    return first_term + second_term

highest_term = 100
set_l1 = 0
set_l2 = 0
set_l3 = 0

for l1 in range(0, 300, 2):
    l1 = l1 / 10
    for l2 in range(0, 300, 2):
        l2 = l2 / 10
        for l3 in range(0, 300, 2):
            l3 = l3 / 10
            temp_result = lasso(X, Y, l1, l2, l3, 1, 3)
            if temp_result < highest_term:
                highest_term = temp_result
                set_l1 = l1
                set_l2 = l2
                set_l3 = l3

print(f"The lasso coefficients for l1 is {set_l1}, l2 is {set_l2}, l3 is {set_l3}")