# Semesters Required - Graph Problem
# Calculate minimum semesters needed (topological sort)

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long as the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.


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
def semesters_required(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)
  distance = {}
  for course in range(num_courses):
    if len(graph[course]) == 0:
      distance[course] = 1
  
  for course in range(num_courses):
    traverse_distance(graph, course, distance)
    
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  max_distance = 0
  for neighbor in graph[node]:
    neighbor_distance = traverse_distance(graph, neighbor, distance)
    if neighbor_distance > max_distance:
      max_distance = neighbor_distance
    
  distance[node] = 1 + max_distance
  return distance[node]

def build_graph(num_courses, prereqs):
  graph = {}
  
  for course in range(num_courses):
    graph[course] = []
    
  for prereq in prereqs:
    a, b = prereq
    graph[a].append(b)
  
  return graph
