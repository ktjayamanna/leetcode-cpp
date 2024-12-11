'''
| Graph Type              | Key Change                                                             |
|-------------------------|------------------------------------------------------------------------|
| Directed Acyclic (DAG)   | Standard BFS with `visited` set, stops when the destination is found.  |
| Undirected Acyclic (Tree)| Tracks `parent` to avoid backtracking.                                |
| Directed Cyclic          | Same as DAG, but `visited` ensures no infinite loops.                |
| Undirected Cyclic        | Uses `parent` to prevent cycles and infinite revisits.               |
'''

from collections import deque

### 1. **Directed Acyclic Graph (DAG)**

def bfs_dag(graph, src, dst, visited=set()):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                queue.append(neighbor)
    return False


### 2. **Undirected Acyclic Graph (Tree)**

def bfs_tree(graph, src, dst):
    queue = deque([(src, None)])  # Track parent to avoid backtracking
    visited = set()

    while queue:
        current, parent = queue.popleft()
        if current == dst:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor != parent:  # Avoid revisiting the parent
                    queue.append((neighbor, current))
    return False

### 3. **Directed Cyclic Graph**


def bfs_directed_cyclic(graph, src, dst):
    queue = deque([src])
    visited = set()

    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                queue.append(neighbor)
    return False


### 4. **Undirected Cyclic Graph**


def bfs_undirected_cyclic(graph, src, dst):
    queue = deque([(src, None)])  # Track parent to avoid backtracking
    visited = set()

    while queue:
        current, parent = queue.popleft()
        if current == dst:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor != parent:  # Avoid revisiting the parent
                    queue.append((neighbor, current))
    return False





