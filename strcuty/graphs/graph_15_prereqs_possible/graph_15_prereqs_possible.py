# Prereqs Possible - Graph Problem
# Check if prerequisites can be satisfied (cycle detection)

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses.


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
def prereqs_possible(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)
  visiting = set()
  visited = set()
  
  for node in range(0, num_courses):
    if has_cycle(graph, node, visiting, visited):
      return False
    
  return True
  
def has_cycle(graph, node, visiting, visited):
  if node in visited:
    return False
  
  if node in visiting:
    return True
  
  visiting.add(node)
  
  for neighbor in graph[node]:
    if has_cycle(graph, neighbor, visiting, visited):
      return True
  
  visiting.remove(node)
  visited.add(node)
  
  return False


def build_graph(num_courses, prereqs):
  graph = {}
  
  for i in range(0, num_courses):
    graph[i] = []
    
  for prereq in prereqs:
    a, b = prereq
    graph[a].append(b)
    
  return graph
