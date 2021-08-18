# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:32:56 2020

@author: Grant
"""

data_points = [[1, 3], [2, 5], [3, 10], [6, 19], [9, 28], [8, 25]]

class functions:
    def __init__(self, input_data):
        self.data = input_data
    
    def first_function(self):
        result = []
        
        for a in self.data:
            temp = []
            temp.append(a[0])
            y = a[0]
            temp.append((y - a[1])**2)
            
            result.append(temp)
        
        return result
    
    def second_function(self):
        result = []
        
        for a in self.data:
            temp = []
            temp.append(a[0])
            y = 2*(a[0])
            temp.append((y - a[1])**2)
            
            result.append(temp)
        
        return result
    
    def third_function(self):
        result = []
        
        for a in self.data:
            temp = []
            temp.append(a[0])
            y = 3*(a[0])
            temp.append((y - a[1])**2)
            
            result.append(temp)
        
        return result
    
    def fourth_function(self):
        result = []
        
        for a in self.data:
            temp = []
            temp.append(a[0])
            y = 4*(a[0])
            temp.append((y - a[1])**2)
            
            result.append(temp)
        
        return result
    
    def fifth_function(self):
        result = []
        
        for a in self.data:
            temp = []
            temp.append(a[0])
            y = 5*(a[0])
            temp.append((y - a[1])**2)
            
            result.append(temp)
        
        return result
    
    def sixth_function(self):
        result = []
        
        for a in self.data:
            temp = []
            temp.append(a[0])
            y = 6*(a[0])
            temp.append((y - a[1])**2)
            
            result.append(temp)
        
        return result

functions_set = functions(data_points)
losses = []
losses.append(functions_set.first_function())
losses.append(functions_set.second_function())
losses.append(functions_set.third_function())
losses.append(functions_set.fourth_function())
losses.append(functions_set.fifth_function())
losses.append(functions_set.sixth_function())

risks = []
function_number = 1
for a in losses:
    len_temp = len(a)
    sum_temp = 0
    risk_temp = 0
    risk_array_temp = []
    
    for b in a:
        sum_temp += b[1]
    
    risk_temp = sum_temp/len_temp
    risk_array_temp.append(function_number)
    risk_array_temp.append(risk_temp)
    
    risks.append(risk_array_temp)
    function_number += 1

risks.sort(key=lambda x: x[1])

print(f"Method {risks[0][0]} is the most suitable.")
    
    
    