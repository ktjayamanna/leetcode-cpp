# Union Find Code I - Graph Problem
# Implementing union find data structure part 1

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, count_components, that takes in a number of nodes (n) and a list of edges for an undirected graph. In the graph, nodes are labeled from 0 to n - 1. 
The function should return the number of connected components in the given graph.

EXAMPLES:
================================================================================
count_components(7, [
  (0, 2),
  (1, 0),
  (4, 3),
  (2, 5),
  (3, 6)
]) # -> 2
count_components(100, [
  (50, 60),
  (80, 20)
]) # -> 98


COMPLEXITY:
================================================================================


"""

# SOLUTION:
# ================================================================================
# Iterative with no path compression
def count_components(n, edges):
  graph = {i : i for i in range(n)}
  for a, b in edges:
    a, b  = find(graph, a), find(graph, b)
    union(graph, a, b)
  count = 0
  for node in graph:
    if graph[node] == node:
      count += 1
  return count

def union(graph, a, b):
  graph[a] = b
    

def find(graph, a):
  while graph[a] != a:
    a = graph[a]
  return a

# Recursive: Alvin's
def find(roots, node):
  if node == roots[node]:
    return node
  return find(roots, roots[node])

def union(roots, node_a, node_b):
  root_a = find(roots, node_a)
  root_b = find(roots, node_b)
  roots[root_b] = root_a
      
def count_components(n, edges):
  roots = [ i for i in range(0, n) ]
  
  for edge in edges:
    node_a, node_b = edge
    union(roots, node_a, node_b)

  count = 0
  for i in range(0, len(roots)):
    if i == roots[i]:
      count += 1
      
  return count

    

