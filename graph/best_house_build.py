'''
You are building a new house in the neighborhood and want to choose a location so that the house is as close as possible to all other houses.

Write a function, best_house_build, that takes in a grid. In the grid, 0's are empty spaces, 1's are houses, and 2's are trees. Your job is to find an empty space on the grid that has the shortest total travel distance to all houses. Your function should return a number that corresponds to this shortest total travel distance. If it is not possible to choose a location that is that is reachable by all houses, then return -1.

When calculating the distance, you can only move up, down, left, or right. You may not pass through houses or trees.

'''
from collections import deque

def best_house_build(grid):
  houses = set()
  trees = set()
  empty = dict()
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == 1:
        houses.add((row, col))
      elif grid[row][col] == 2:
        trees.add((row, col))
      else:
        empty[(row, col)] = 0

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      key = (row, col)
      if key not in houses and key not in trees:
        unreachable = False
        for house in houses:
          visited = set()
          dst_row, dst_col = house
          distance = bfs(grid, row, col, dst_row, dst_col, visited)
          if distance == 0:  # If any house is unreachable
            unreachable = True
            break
          empty[key] += distance

        # Mark locations with unreachable houses as invalid
        if unreachable:
          empty[key] = float('inf')

  print(empty)
  # If all locations have unreachable houses, return -1
  min_distance = min(empty.values()) if empty else float('inf')
  return min_distance if min_distance != float('inf') else -1

def bfs(grid, start_row, start_col, dst_row, dst_col, visited):
  queue = deque([(start_row, start_col, 0)])
  while queue:
    row, col, dist = queue.popleft()

    visited.add((row, col))
    directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
    for r, c in directions:
      new_row = row + r
      new_col = col + c
      if is_in_bound(grid, new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] != 2:
        if (new_row, new_col) == (dst_row, dst_col):
          return dist + 1
        elif grid[new_row][new_col] != 1:
          queue.append((new_row, new_col, dist + 1))
  return 0

def is_in_bound(grid, row, col):
  return 0 <= row and row < len(grid) and 0 <= col and col < len(grid[0])


grid = [
  [0,0,0,1,0,0,0,0],
  [0,1,0,0,0,0,0,0],
  [0,0,0,1,0,2,2,2],
  [0,0,0,0,0,2,0,0],
  [0,0,0,0,0,2,0,1]
]
print(best_house_build(grid)) # -> -1




