#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:38:06 2020

@author: yuchenzhang
"""

graph = {"A":["B","C","D"], "B":["E","F"], "C":"G","D":"C", "E":"F","F":"E","G":"C"}

def bfs(graph, start):
    
    explored = [];
    queue = [start];
    while queue:
        node = queue.pop(0);
        if node not in explored:
            explored.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    return explored