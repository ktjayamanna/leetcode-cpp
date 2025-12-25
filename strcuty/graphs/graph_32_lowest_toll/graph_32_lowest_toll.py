# Lowest Toll - Graph Problem
# Find the path with the lowest toll cost

"""
PROBLEM DESCRIPTION:
================================================================================
You are given the tolls for different highways. Each highway connects a pair of cities and has a particular cost that must be paid to use it.

Each highway toll is a triplet (cityA, cityB, cost). Every highway can be traveled in either direction.

Write a function that takes in highway tolls and two cities.
 
The function should return the lowest cost required to travel between the two cities. You can assume that there exists at least one way to travel between the two cities.

EXAMPLES:
================================================================================
highway_tolls = [
  ("Hampton", "Fairfax", 7.50),
  ("Roanoake", "Alexandria", 4.20),
  ("Alexandria", "Hampton", 14.50),
  ("Hampton", "Roanoake", 8.90),
  ("Alexandria", "Fairfax", 5.90),
  ("Hampton", "Manassas", 3.50),
  ("Fairfax", "Manassas", 2.20),
]
lowest_toll(highway_tolls, "Alexandria", "Hampton") # -> 11.60

highway_tolls = [
  ("Hampton", "Fairfax", 7.50),
  ("Roanoake", "Alexandria", 4.20),
  ("Alexandria", "Hampton", 14.50),
  ("Hampton", "Roanoake", 8.90),
  ("Alexandria", "Fairfax", 5.90),
  ("Hampton", "Manassas", 3.50),
  ("Fairfax", "Manassas", 2.20),
]
lowest_toll(highway_tolls, "Alexandria", "Fairfax") # -> 5.90


COMPLEXITY:
================================================================================
n = number of cities
Time: O(n!)
Space: O(n^2)

"""

# SOLUTION:
# ================================================================================
def lowest_toll(highway_tolls, start_city, end_city):
  graph = {}
  for city_a, city_b, cost in highway_tolls:
    if city_a not in graph:
      graph[city_a] = {}
    if city_b not in graph:
      graph[city_b] = {}
    graph[city_a][city_b] = cost
    graph[city_b][city_a] = cost

  return min_path(graph, start_city, end_city, set())

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
    if total_cost < min_cost:
      min_cost = total_cost

  visited.remove(src)
  return min_cost


