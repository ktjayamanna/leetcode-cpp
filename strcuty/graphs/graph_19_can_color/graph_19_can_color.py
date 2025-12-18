# Can Color - Graph Problem
# Determine if a graph can be colored with a given number of colors

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph. 
The function should return a boolean indicating whether or not it is possible to color nodes of the graph using two colors in such a way that adjacent nodes are always different colors.

EXAMPLES:
================================================================================
For example, given this graph:

x-y-z

It is possible to color the nodes by using red for x and z, 
then use blue for y. So the answer is True.

For example, given this graph:

    q
   / \
  s - r

It is not possible to color the nodes without making two 
adjacent nodes the same color. So the answer is False.
can_color({
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
}) # -> True
can_color({
  "a": ["b", "c", "d"],
  "b": ["a"],
  "c": ["a"],
  "d": ["a"],
}) # -> True


COMPLEXITY:
================================================================================
n = number of nodes
Time: O(n^2)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
def can_color(graph):
  coloring = {}
  for node in graph:
    if node not in coloring:
      if not valid(graph, node, coloring, False):
        return False
      
  return True

def valid(graph, node, coloring, current_color):
  if node in coloring:
    return current_color == coloring[node]
  
  coloring[node] = current_color
  
  for neighbor in graph[node]:
    if not valid(graph, neighbor, coloring, not current_color):
      return False
    
  return True


