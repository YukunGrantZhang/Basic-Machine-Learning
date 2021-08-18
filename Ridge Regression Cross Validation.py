# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:15:58 2020

@author: Grant
"""

import numpy

training_data_x = [[1, 5, 6], [2, 8, 9], [6, 5, 8], [8, 1, 3], [3, 6, 8]]
#training_data_y = [[86], [241], [1163], [2566], [251]]
training_data_y = [[83], [245], [1161], [2588], [253]]
training_data_size = len(training_data_x)

test_data_x = [11, 5, 6]
test_data_y = 6736

error = []
error_element = []
error_sk = []

for L in range(0, 30, 1):
    L = L / 10
    print(L)
    
    error_sk.clear()
    
    for i in range(training_data_size):
        temp_data_x = training_data_x[:]
        temp_data_y = training_data_y[:]
        
        validation_element_x = temp_data_x[i]
        validation_element_y = temp_data_y[i]
        
        temp_data_x.pop(i)
        temp_data_y.pop(i)
        
        temp_X = []
        for a in temp_data_x:
            temp_entry = []
            temp_entry.append(a[0]**3)
            temp_entry.append(a[1]**2)
            temp_entry.append(a[2])
            temp_X.append(temp_entry)

        X = numpy.array(temp_X)
        Y = numpy.array(temp_data_y)
        n = 3
        temp_I = [n*L, 0, 0], [0, n*L, 0], [0, 0, n*L]
        I = numpy.array(temp_I)

        w_1 = numpy.linalg.inv(numpy.add(numpy.dot(X.T, X), I)) 
        w_2 = numpy.dot(X.T, Y)
        w = numpy.dot(w_1, w_2)
        print("The weights are:", w[0], w[1], w[2])
        
        v_y =  w[0][0]*(validation_element_x[0])**3 + w[1][0]*(validation_element_x[1])**2 + w[2][0]*validation_element_x[2]
        print(abs(v_y - validation_element_y[0]))
        error_sk.append(abs(v_y - validation_element_y[0]))
    
    temp_error = sum(error_sk) / training_data_size
    print(temp_error)
    print(error_sk)
    
    error_element.clear()
    error_element.append(L)
    error_element.append(temp_error)
    print(error_element)
    error_input = error_element[:]
    error.append(error_input)

error.sort(key = lambda x: x[1])

print(error)

print(f"The best lambda to choose is {error[0][0]}")

temp_X_new = []
for a in training_data_x:
    temp_entry = []
    temp_entry.append(a[0]**3)
    temp_entry.append(a[1]**2)
    temp_entry.append(a[2])
    temp_X_new.append(temp_entry)

X_new = numpy.array(temp_X_new)
Y_new = numpy.array(training_data_y)
n = 3
L = error[0][0]
temp_I_new = [n*L, 0, 0], [0, n*L, 0], [0, 0, n*L]
I_new = numpy.array(temp_I_new)

w_1_new = numpy.linalg.inv(numpy.add(numpy.dot(X_new.T, X_new), I_new)) 
w_2_new = numpy.dot(X_new.T, Y_new)
w_new = numpy.dot(w_1_new, w_2_new)
print("The new weights are:", w_new[0], w_new[1], w_new[2])

y_temp = w_new[0][0]*(test_data_x[0])**3 + w_new[1][0]*(test_data_x[1])**2 + w_new[2][0]*test_data_x[2]

print("Error between training and test datasets are", abs(y_temp - test_data_y)/test_data_y)