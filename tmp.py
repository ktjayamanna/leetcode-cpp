def best_bridge(grid):
  start_row, start_col = find_starting_point(grid)
  main_island_nodes = dict()
  dfs(grid, start_row, start_col, main_island_nodes)
  for node in main_island_nodes.keys():
    start_row, start_col = node
    main_island_nodes[node] = bfs(grid, start_row, start_col, main_island_nodes)
  print(main_island_nodes)
  return min(main_island_nodes.values())

def find_starting_point(grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "L":
        return (i, j)

def check_bounds(grid, row, col):
  return 0 <= row < len(grid) and 0 <= col <  len(grid[0])


def dfs(grid, row, col, main_island_nodes):
  if not check_bounds(grid, row, col) or (row, col) in main_island_nodes or grid[row][col] == "W":
    return None
  main_island_nodes[(row, col)] = 0
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  for dr, dc in directions:
    new_row = row + dr
    new_col = col + dc
    dfs(grid, new_row, new_col, main_island_nodes)  
  return None


from collections import deque

def bfs(grid, row, col, main_island_nodes):
  queue = deque([(row, col, 0)])
  visited = {(row, col)}
  while queue:
    print(queue)
    row, col, distance = queue.popleft()
    if grid[row][col] == 'L' and (row, col) not in main_island_nodes:
      return distance - 1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in directions:
      new_row = row + dr
      new_col = col + dc
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

    