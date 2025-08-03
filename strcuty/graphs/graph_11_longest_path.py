# Longest Path - Graph Problem
# Find the longest path in a graph

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.


EXAMPLES:
================================================================================
[Add examples here]


CONSTRAINTS:
================================================================================
[Add constraints here]

"""

# SOLUTION:
# ================================================================================
# [Add your Python solution here]
def longest_path(graph):
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0
      
  for node in graph:
    traverse_distance(graph, node, distance)
    
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  largest = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > largest:
      largest = attempt
  
  distance[node] = 1 + largest
  return distance[node]
