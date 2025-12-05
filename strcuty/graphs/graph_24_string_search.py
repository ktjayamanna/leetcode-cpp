# String Search - Graph Problem
# Search for strings in a graph structure

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, string_search, that takes in a grid of letters and a string as arguments. 
The function should return a boolean indicating whether or not the string can be found in the grid as a path by connecting horizontal or vertical positions. 
The path can begin at any position, but you cannot reuse a position more than once in the path.

You can assume that all letters are lowercase and alphabetic.

EXAMPLES:
================================================================================
grid = [
  ['a', 'b', 'a'],
  ['t', 'x', 'x'],
  ['x', 'x', 'x'],
];
string_search(grid, 'abat') # -> true


COMPLEXITY:
================================================================================
r = # grid rows
c = # grid columns
Time: O(3^(r*c))
Space: O(r*c)

"""

# SOLUTION:
# ================================================================================
# My solution
def string_search(grid, s):
  visited = set()
  idx = 0
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if dfs(grid, s, row, col, idx, visited):
          return True
  return False

def dfs(grid, s, row, col, idx, visited):
  key = (row, col)
  if idx == len(s):
    return True
  if key in visited:
    return False
  visited.add(key)
  if s[idx] != grid[row][col]:
    return False
  directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
  for r, c in directions:
    new_row, new_col = row + r, col + c
    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
      if dfs(grid, s, new_row, new_col, idx + 1, visited):
        return True
  visited.remove(key)
  return False

# Alvin's solution
def string_search(grid, s):
  for r in range(len(grid)):
    for c in range(len(grid[0])):    
      if dfs(grid, r, c, s):
        return True
  return False


def dfs(grid, r, c, s):
  if s == '':
    return True
  
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return False
  
  char = grid[r][c]
  if char != s[0]:
    return False
  
  suffix = s[1:]
  
  grid[r][c] = '*'
  
  result = dfs(grid, r + 1, c, suffix) or dfs(grid, r - 1, c, suffix) or dfs(grid, r, c + 1, suffix) or dfs(grid, r, c - 1, suffix)
  grid[r][c] = char
  return result

  
  
      

