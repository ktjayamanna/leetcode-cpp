def island_count(grid):
  islands = 0
  visited = set()
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if explore_dfs(grid, row, col, visited):
        islands += 1
  return islands

def explore_dfs(grid, row, col, visited):
  row_bounds = 0 <= row < len(grid)
  col_bounds = 0 <= col < len(grid[0])

  if not row_bounds or not col_bounds:
    return False
    
  current = f'{row}{col}'
  
  if current in visited:
    return False
  else:
    visited.add(current)

  if grid[row][col] == "W":
    return False
  else:
    explore_dfs(grid, row - 1, col, visited)
    explore_dfs(grid, row + 1, col, visited)
    explore_dfs(grid, row, col - 1, visited)
    explore_dfs(grid, row, col + 1, visited)
  
  return True
  
      