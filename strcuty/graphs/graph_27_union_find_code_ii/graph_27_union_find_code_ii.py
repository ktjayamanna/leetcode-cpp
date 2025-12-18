# Union Find Code II - Graph Problem
# Implementing union find data structure part 2

"""
PROBLEM DESCRIPTION:
================================================================================

Write a function, countComponents, that takes in a number of nodes (n) and a list of edges for an undirected graph. 
In the graph, nodes are labeled from 0 to n - 1. 
The function should return the number of connected components in the given graph.

Solve this by implementing the complete Union-Find algorithm with size and path-compression.

EXAMPLES:
================================================================================
count_components(10, [
  (3, 2),
  (5, 4),
  (4, 3),
  (2, 1),
  (0, 1),
  (8, 9),
  (5, 6),
  (7, 8)
]) # -> 2

count_components(100, [
  (50, 60),
  (80, 20)
]) # -> 98


COMPLEXITY:
================================================================================
n = # nodes
e = # edges
Time: O(n + e * α(n))
Space: O(n)

"""

# SOLUTION:
# ================================================================================
def find(roots, node):
  if node == roots[node]:
    return node
  found = find(roots, roots[node])
  roots[node] = found
  return found

def union(roots, sizes, node_a, node_b):
  root_a = find(roots, node_a)
  root_b = find(roots, node_b)

  if root_a == root_b:
    return

  if sizes[root_a] >= sizes[root_b]:
    roots[root_b] = root_a
    sizes[root_a] += sizes[root_b]
  else:
    roots[root_a] = root_b
    sizes[root_b] += sizes[root_a]
      
def count_components(n, edges):
  roots = [ i for i in range(0, n) ]
  sizes = [ 1 for i in range(0, n) ]
  
  for edge in edges:
    node_a, node_b = edge
    union(roots, sizes, node_a, node_b)
    
  count = 0
  for i in range(0, len(roots)):
    if i == roots[i]:
      count += 1
      
  return count


