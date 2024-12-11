def connected_components_count(graph):
  visited = set()
  components = 0
  
  for node in graph.keys():
    if dfs(graph, node, visited):
      components += 1
      
  return components
      

def dfs(graph, src, visited):
  if src in visited:
    return False
    
  visited.add(src)
  
  for neighbor in graph[src]:
    dfs(graph, neighbor, visited)
    
  return True
  