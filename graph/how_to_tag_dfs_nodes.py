'''
Kinda like how you tag distance in Queue for BFS, 
you tag distances in dfs using a global hash map that serves 
the both visited and distance information purposes.
'''

def longest_path(graph):
  distance_map = initialize_map(graph)
  for node in graph.keys():
    dfs(graph, node, distance_map)
  return max(distance_map.values())

def initialize_map(graph):
  distance_map = dict()
  for node in graph.keys():
    if not len(graph[node]):
      distance_map[node] = 0
  return distance_map      

def dfs(graph,node, distance_map):
  if node in distance_map:
    return distance_map[node]
  longest = float("-inf")
  for neighbor in graph[node]:
    path_len = dfs(graph, neighbor, distance_map)
    if longest < path_len:
      longest = path_len
  distance_map[node] = longest + 1
  return distance_map[node]