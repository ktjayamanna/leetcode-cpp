# Weighted Graph Min Path - Graph Problem
# Find the minimum path in a weighted graph

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function that takes in the adjacency list for a weighted graph and two nodes, src and dst. 
The function should return the minimum cost path that travels from src to dst.
The cost of a path is the sum of the weights of edges traveled.
You can assume that the weights are non-negative numbers and there is at least one path between src and dst.

EXAMPLES:
================================================================================
graph = {
  "a": { "b": 2, "d": 9, "c": 5 },
  "b": { "a": 2, "d": 4, "e": 6 },
  "c": { "a": 5, "e": 4 },
  "d": { "a": 9, "b": 4, "e": 1 },
  "e": { "b": 6, "c": 4, "d": 1 },   
}
weighted_graph_min_path(graph, "a", "e") # -> 7

graph = {
  "q": { "r": 5, "s": 10 },
  "r": { "q": 5, "s": 9, "u": 2 },
  "s": { "q": 10, "r": 9, "t": 1, "v": 8 },
  "t": { "s": 1 },
  "u": { "r": 2, "s": 1 },
  "v": {}, 
}
weighted_graph_min_path(graph, "q", "v") # -> 16

graph = {
  "q": { "r": 5, "s": 10 },
  "r": { "q": 5, "s": 9, "u": 2 },
  "s": { "q": 10, "r": 9, "t": 1, "v": 8 },
  "t": { "s": 1 },
  "u": { "r": 2, "s": 1 },
  "v": {}, 
}
weighted_graph_min_path(graph, "r", "v") # -> 11


COMPLEXITY:
================================================================================
n = number of nodes
Time: O(n!)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
def weighted_graph_min_path(graph, src, dst):
  return min_path(graph, src, dst, set())

def min_path(graph, src, dst, visited):
  if src == dst:
    return 0

  if src in visited:
    return float("inf")
  visited.add(src)
  
  min_cost = float("inf")
  for neighbor in graph[src]:
    cost = graph[src][neighbor]
    total_cost = cost + min_path(graph, neighbor, dst, visited)
    min_cost = min(min_cost, total_cost)
    
  visited.remove(src)
  return min_cost


