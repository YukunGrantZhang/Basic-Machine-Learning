# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:57:54 2020

@author: Grant
"""
   
from collections import defaultdict 
from numpy import prod
import math

weights = []

def sum_and_clear():
    global weights
    
    answer = sum(weights)
    
    weights.clear()
    
    return answer
 
class Graph: 
   
    def __init__(self, vertices): 
        self.V = vertices  
          
        self.graph = defaultdict(list)
        self.weight = defaultdict(list) 
   
    def addEdge(self, u, v, w): 
        self.graph[u].append(v)
        self.weight[u].append(w)
   
    def AllPathsUtil(self, u, d, visited, path, weight): 
        visited[u]= True
        path.append(u)
        
        if u == d: 
            weights.append(prod(weight))
        else: 
            for i in range(len(self.graph[u])): 
                if visited[self.graph[u][i]]== False:
                    weight.append(self.weight[u][i])
                    self.AllPathsUtil(self.graph[u][i], d, visited, path, weight) 
                     
        path.pop() 
        if len(weight) > 0:
            weight.pop()
        visited[u]= False
   
    def AllPaths(self, s, d): 
        visited =[False]*(self.V) 
  
        path = [] 
        weight = []
  
        self.AllPathsUtil(s, d, visited, path, weight) 
   
def graph_kernel(s, d):
    g.AllPaths(s, d)
    part_1 = sum_and_clear()
    
    g.AllPaths(d, s)
    part_2 = sum_and_clear()

    return part_1 + part_2
   
number_of_vertices = 5
g = Graph(number_of_vertices) 
g.addEdge(0, 1, 0.3) 
g.addEdge(0, 2, 0.1) 
g.addEdge(1, 4, 0.1)
g.addEdge(2, 1, 0.6)  
g.addEdge(3, 0, 0.8)
g.addEdge(4, 3, 0.5) 
   
s = 0 ; d = 4 
graph_kernel(s, d)

C = 8
n = number_of_vertices

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
                    
                    sum_1 = a1 + a2 + a3 + a4 + a5
                
                    temp_alphas.clear()
                    temp_alphas = [a1, a2, a3, a4, a5]
                
                    sum_2 = 0
                
                    for i in range(number_of_vertices):
                        for j in range(number_of_vertices):
                            sum_2 += (temp_alphas[i] * temp_alphas[j] * graph_kernel(i, j))
                    
                    sum_2 = sum_2 / 2
                
                    total = sum_1 - sum_2
                
                    result.append([a1, a2, a3, a4, a5, total])
                
result.sort(key=lambda x:x[5], reverse = True)

w = 0
for a in range(number_of_vertices):
    w += result[0][a]
    
b = 0
for j in range (number_of_vertices):
    sum_1 = 1
    sum_2 = 0
    for i in range(number_of_vertices):
        sum_2 += result[0][i] * graph_kernel(i, j)
    
    temp_sum = sum_1 - sum_2
    
    b += (temp_sum / (number_of_vertices)) 

print(f"The line is y = {w}x + {b}")
