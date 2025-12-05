# Union Find Code I - Graph Problem
# Implementing union find data structure part 1

"""
PROBLEM DESCRIPTION:
================================================================================


EXAMPLES:
================================================================================


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


