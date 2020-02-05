#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:37:13 2020

@author: yuchenzhang
"""

graph_shortest_path = {'A':['B','C','D'],'B':['A','E','F'],'C':'A', 
                       'D':['A', 'H'], 'E':['B', 'G'], 'F':['B','H'], 
                       'G':['E', 'H'],'H':['D','F','G']}

def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        print ("The start is the end. Search done!")
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbors = graph[node]
        for neighbor in neighbors:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
            if neighbor == goal:
                print("Found the goal state!")
                return new_path
        explored.append(node)