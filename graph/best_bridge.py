'''
Write a function, best_bridge, that takes in a grid as an argument. The grid contains water (W) and land (L). There are exactly two islands in the grid. An island is a vertically or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.

Input:  takes in a grid as an argument. The grid contains water (W) and land (L)
Input Type: List(List, List... List)
Output:  Return the minimum length bridge needed to connect the two islands
Output Type: int
Interesting facts:
- There are exactly two islands in the grid.
- An island is a vertically or horizontally connected region of land.
-  A bridge does not need to form a straight line.

'''

def best_bridge(grid):
    # Find the first island and mark its cells
    island = {}
    row, col = find_first_land(grid)
    dfs(grid, row, col, island)

    # Calculate the minimum bridge length for all island cells
    for r, c in island:
        island[(r, c)] = bfs(grid, r, c, island)

    return min(island.values())

def find_first_land(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "L":
                return row, col  # Return immediately when land is found
    return None  # Return None if no land is found


def check_bounds(grid, row, col):
  return 0 <= row < len(grid) and 0 <= col < len(grid[0])



def dfs(grid, row, col, island):
    # Check if current position is valid and not already visited or water
    if (not check_bounds(grid, row, col) 
            or grid[row][col] == 'W' 
            or (row, col) in island):
        return

    # Mark the current cell as visited
    island[(row, col)] = 0

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Explore all neighboring cells
    for d_row, d_col in directions:
        dfs(grid, row + d_row, col + d_col, island)

    return island

  
from collections import deque

def bfs(grid, start_row, start_col, island):
    visited = {(start_row, start_col)}
    queue = deque([(start_row, start_col, 0)])

    while queue:
        row, col, distance = queue.popleft()

        # If we hit land not in our starting island, we've completed the bridge
        if grid[row][col] == 'L' and (row, col) not in island:
            return distance - 1

        # Always explore neighbors, even if this cell is water
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in deltas:
            new_row, new_col = row + dr, col + dc
            if check_bounds(grid, new_row, new_col) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))



grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
print(best_bridge(grid)) # -> 1
island = dict()
print(dfs(grid, 0, 3, island))
















    

