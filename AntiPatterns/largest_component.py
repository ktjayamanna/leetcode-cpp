'''
Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.

largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4

Input: Adjecncy list of an undirected graph
Input Type: dict(int -> [int, int ...])
Input Preprocessing: None
Algorithm: 
1) We need find the size of a component.
2) We need to find the largest size.
3) We need to discover components from the graph.
4) We need to travese the graph using dfs.
5) We need to avoid cycles.

- global max
- every component you discover, compare it's size to the max and swap if needed.
- use dfs and if the traversal completes returns it's size. 
- traversal is complete if all the neightbors are visited. If the current node is visited, return 0.
- pass in a variable to keep track of the size of the current component and retun the size when you hit base case.
- Iteratively run dfs on all nodes to see if they form a seperate component.


Output: size of the largest connected component in the graph
Output type: int
Keywords:  largest_component, adjacency list, undirected graph, size

'''
# My initial solution which is wrong
def largest_component(graph):
  max_size = float('-inf')
  visited = set()
  
  for node in graph.keys():
    current_size = 0
    current_size = dfs(graph, node, visited, current_size)
    if current_size > max_size:
      max_size = current_size
  return max_size
      

def dfs(graph, src, visited, current_size):
  if src in visited:
    return 0
  else:
    visited.add(src)
    current_size +=1
    
  for neightbor in graph[src]:
    current_size += dfs(graph, neightbor, visited, current_size)
  
  return current_size

# Instead of using a global variable, we should use a local variable because it gets modified a lot.

def largest_component(graph):
  largest_component = 0
  visited = set()
  for node in graph.keys():
    current_size = dfs(graph, node, visited)
    if current_size > largest_component:
      largest_component = current_size
  return largest_component


def dfs(graph, src, visited):
  current_size = 0
  if src in visited:
    return current_size
  visited.add(src)
  current_size += 1
  for neighbor in graph[src]:
    current_size += dfs(graph, neighbor, visited)
  return current_size
  
  

















