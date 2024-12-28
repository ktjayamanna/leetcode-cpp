from collections import deque

### 1. **Directed Acyclic Graph (DAG)**
def bfs_dag(graph, start, visited=set(), result=None):
    if result is None:
        result = []
    queue = deque([start])
    visited = visited
    
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            result.append(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

### 2. **Undirected Acyclic Graph (Tree)**
def bfs_tree(root):
    if not root:
        return []
    
    queue = deque([root])
    values = []
    
    while queue:
        node = queue.popleft()
        values.append(node.val)
        
        for child in node.children:
            queue.append(child)
            
    return values

### 3. **Directed Cyclic Graph**
def bfs_directed_cyclic(graph, start, visited=set(), result=None):
    if result is None:
        result = []
    queue = deque([start])
    visited = visited.copy()
    
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            result.append(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

### 4. **Undirected Cyclic Graph**
def bfs_undirected_cyclic(graph, start, visited=set(), result=None):
    if result is None:
        result = []
    queue = deque([(start, None)])  # (node, parent)
    visited = visited.copy()
    
    while queue:
        current, parent = queue.popleft()
        if current not in visited:
            visited.add(current)
            result.append(current)
            for neighbor in graph[current]:
                if neighbor != parent:
                    queue.append((neighbor, current))
    return result