'''
| Graph Type              | Key Change                                                                 |
|-------------------------|----------------------------------------------------------------------------|
| Directed Acyclic (DAG)   | Regular DFS with `visited` set, post-order processing for topological sort |
| Undirected Acyclic (Tree)| Use a `parent` parameter to avoid backtracking                           |
| Directed Cyclic          | Use `rec_stack` to detect cycles                                         |
| Undirected Cyclic        | Use `parent` and check for revisits to detect cycles                     |

'''


### 1. **Directed Acyclic Graph (DAG)**

# For a **DAG**, we use the `visited` set to ensure we don't reprocess nodes, and we can collect results in post-order for applications like **topological sorting**.

def dfs_dag(graph, start, visited=set(), result=None):
    if result is None:
        result = []
    if start in visited:
        return
    visited.add(start)
    for neighbor in graph[start]:
        dfs_dag(graph, neighbor, visited, result)
    result.append(start)  # Post-order processing
    return result


### 2. **Undirected Acyclic Graph (Tree)**

# In an **undirected acyclic graph** (tree), we need to pass the `parent` node to avoid traversing back to it since there are no explicit directions.

def dfs_tree(graph, start, parent=None, visited=set(), result=None):
    if result is None:
        result = []
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor != parent:  # Avoid going back to the parent
            dfs_tree(graph, neighbor, start, visited, result)
    result.append(start)  # Post-order processing
    return result


### 3. **Directed Cyclic Graph**

# For a **directed cyclic graph**, we need to detect cycles. A common approach is to use two sets:
# - `visited`: To track all nodes that have been fully processed.
# - `rec_stack`: To track nodes in the current recursive stack (used to detect cycles).

def dfs_directed_cyclic(graph, start, visited=set(), rec_stack=set(), result=None):
    if result is None:
        result = []
    if start in rec_stack:
        raise ValueError("Cycle detected in the graph!")
    if start in visited:
        return
    rec_stack.add(start)
    for neighbor in graph[start]:
        dfs_directed_cyclic(graph, neighbor, visited, rec_stack, result)
    rec_stack.remove(start)
    visited.add(start)
    result.append(start)  # Post-order processing
    return result


### 4. **Undirected Cyclic Graph**

# In an **undirected graph**, cycles occur when we visit a previously visited node that isn't the immediate parent. We use the `parent` parameter to distinguish back edges from tree edges.

def dfs_undirected_cyclic(graph, start, parent=None, visited=set(), result=None):
    if result is None:
        result = []
    if start in visited:
        return
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor != parent:  # Avoid going back to the parent
            if neighbor in visited:
                raise ValueError("Cycle detected in the graph!")
            dfs_undirected_cyclic(graph, neighbor, start, visited, result)
    result.append(start)  # Post-order processing
    return result



