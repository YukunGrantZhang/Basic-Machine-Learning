# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:54:15 2020

@author: Grant
"""

input_points = [[5, 5, 5], [5, 4, 5], [5, 3, 5], [4, 5, 4], [4, 4, 4], [4, 3, 4], [3, 5, 3], [3, 4, 3], [3, 3, 3], [2, 5, 2], [2, 4, 2], [2, 3, 2]] 

import numpy

class Node:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

class Graph:
	def __init__(self, edges):

		self.adj = [None] * len(edges)

		for i in range(len(edges)):
			self.adj[i] = []

		for e in edges:
			node = Node(e[1], e[2])
			self.adj[e[0]].append(node)

edges = [[0, 1, 2], [0, 2, 4], [1, 3, 2],
		[1, 2, 1], [2, 4, 4], [3, 4, 2]]

graph = Graph(edges)

def BellmanFord(graph, start, length, number_of_vertices):
    A = []

    n = length

    for i in range(0, n + 1):
        A.append([])

    Initial_row = []

    starting_vertex = start

    for i in range(0, n):
        if i == starting_vertex:
            Initial_row.append(0)
        else:
            Initial_row.append(100)

    A[0] = Initial_row
    
    B = []

    n = length

    for i in range(0, n + 1):
        B.append([])
        
    for i in range(0, n):
        B[0].append(None)

    for i in range(1, n + 1):
        for v in range(0, n):
        
            case_1 = A[i - 1][v]
        
            w = []
            e = []
        
            for src in range(len(graph.adj)):
                for edge in graph.adj[src]:
                    if edge.value == v:
                        w.append(src)
                        e.append(edge.weight)
        
            total = []
            for b in range(len(w)):
                total.append(A[i - 1][w[b]] + e[b])
        
            if total != []:
                case_2 = min(total)
                A[i].append(min(case_1, case_2))
                
                chosen_case = min(case_1, case_2)
                
                if chosen_case == case_1:
                    B[i].append(B[i - 1][v])
                else:
                    chosen_index = total.index(min(total))
                    vertex = w[chosen_index]
                    B[i].append(vertex)
            else:
                A[i].append(case_1)
                B[i].append(B[i - 1][v])
        
        if i == n:
            if A[n - 1] != A[n]:
                print("Negative Cycle Detected!")
                return
        
    nodes = [*range(0, n)]
    min_distances = A[len(A) - 1]
    
    return min_distances[0:number_of_vertices]

k = 3

neighbours = []

def nearest_neighbours(training_set):
    global neighbours
    
    for chosen_point in range(len(training_set)):
        points = []
        for comparison_point in range(len(training_set)):
            temp = []
            distance = ((training_set[chosen_point][0] - training_set[comparison_point][0])**2 + (training_set[chosen_point][1] - training_set[comparison_point][1])**2 + (training_set[chosen_point][2] - training_set[comparison_point][2])**2)**(1/2)
            temp.append(chosen_point)
            temp.append(comparison_point)
            temp.append(distance)
            points.append(temp)
        points.sort(key=lambda x: x[2])
        
        chosen_points = points[1:k+1]
        for a in chosen_points:
            neighbours.append(a)
            
nearest_neighbours(input_points)

new_graph = Graph(neighbours)
distance_matrix = []
for a in range(12):
    distance_matrix.append(BellmanFord(new_graph, a, len(neighbours), 12))
print(distance_matrix)












