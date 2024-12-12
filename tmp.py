def largest_element(graph):
  max_val = float("-inf")
  visited = set()
  for node in graph.keys():
    max_val = dfs(graph, node, max_val, visited)
  return max_val


def dfs(graph, src,  max_val, visited ):
  if src in visited:
    return max_val
  else:
    visited.add(src)
  if src > max_val:
    max_val = src
  for neighbor in graph[src]:
    max_val = dfs(graph, neighbor, max_val, visited)
  return max_val
  
graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

print(largest_element(graph))