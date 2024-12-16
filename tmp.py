'''
Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long as the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.

----------------------------------------------------------------------------------------------
Input: takes in a number of courses (n) and a list of prerequisites as arguments
Input Type: int, [(int, int), (int, int)...(int, int)]
Output: Return the minimum number of semesters required to complete all n courses
Output tYpe: int
Interesting things: 
- Courses have ids ranging from 0 through n - 1
- A single prerequisite of (A, B) means that course A must be taken before course B
- no limit on how many courses you can take in a single semester, as long as the prerequisites of a course are satisfied before taking it
- given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.
- assume that it is possible to eventually complete all courses
--------------------------------------------------------------------------------------------------------------------------------------------------------
'''

from collections import deque

def semesters_required(num_courses, prereqs):
  graph = build_graph(prereqs, num_courses)
  start = list(graph.keys())[0]
  num_semesters = bfs(graph, start)
  return num_semesters


def build_graph(prereqs, num_courses):
  graph = {key: [] for key in range(num_courses)}
  for x, y in prereqs:
    if x  in graph:
      graph[x].append(y)
  return graph

def bfs(graph, start):
  queue = deque([start])
  num_levels = 1
  while queue:
    level_size = len(queue)
    for _ in range(level_size):
      current = queue.popleft()
      for neighbor in graph[current]:
        queue.append(neighbor)
      num_levels += 1
  return num_levels


      

