# Save the shortest_path problem and solution into a standalone Python file

shortest_path_code = '''"""
Problem: Shortest Path

Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B).
The function should return the length of the shortest path between A and B.

Consider the length as the number of edges in the path, not the number of nodes.
If there is no path between A and B, then return -1.
You can assume that A and B exist as nodes in the graph.
"""


'''

from collections import deque

def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set([node_A])
    queue = deque([(node_A, 0)])

    while queue:
        node, distance = queue.popleft()

        if node == node_B:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


# === Test Cases ===
print("Test 00")
edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]
print(shortest_path(edges, 'w', 'z'))  # -> 2

print("Test 01")
edges = [
    ['a', 'b'],
    ['b', 'c'],
    ['c', 'd'],
    ['d', 'e'],
    ['e', 'f'],
]
print(shortest_path(edges, 'a', 'e'))  # -> 4

print("Test 02")
edges = [
    ['a', 'b'],
    ['b', 'c'],
    ['c', 'd'],
    ['d', 'e'],
    ['e', 'f'],
]
print(shortest_path(edges, 'a', 'g'))  # -> -1

print("Test 03")
edges = [
    ['a', 'b'],
    ['b', 'c'],
    ['a', 'c'],
    ['c', 'd'],
    ['e', 'f'],
    ['f', 'g'],
]
print(shortest_path(edges, 'e', 'g'))  # -> 2

print("Test 04")
edges = [
    ['a', 'b'],
    ['b', 'c'],
    ['c', 'd'],
    ['d', 'e'],
    ['f', 'g'],
]
print(shortest_path(edges, 'a', 'e'))  # -> 4

print("Test 05")
edges = [
    ['a', 'b'],
    ['b', 'c'],
    ['c', 'd'],
    ['d', 'e'],
    ['f', 'g'],
]
print(shortest_path(edges, 'a', 'f'))  # -> -1