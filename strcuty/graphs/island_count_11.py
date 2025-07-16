"""
Problem: Island Count

Write a function `island_count` that takes in a grid containing 'W's and 'L's.
'W' represents water and 'L' represents land.

The function should return the number of islands on the grid.
An island is a vertically or horizontally connected region of land.
"""

def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count += 1
    return count


def explore(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False

    if grid[r][c] == 'W':
        return False

    pos = (r, c)
    if pos in visited:
        return False
    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True


# === Test Cases ===
print("Test 00")
grid = [
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'L', 'L', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'L', 'W', 'W', 'W'],
]
print(island_count(grid))  # -> 3

print("Test 01")
grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'L'],
]
print(island_count(grid))  # -> 4

print("Test 02")
grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
]
print(island_count(grid))  # -> 1

print("Test 03")
grid = [
    ['W', 'W'],
    ['W', 'W'],
    ['W', 'W'],
]
print(island_count(grid))  # -> 0
