#My solution cleaned by ChatGPT
'''
This solution works great but visited.add((row, col)) line is more error prone 
unless you get the timing perfect. Therefore, always do it when adding to the queue; at least in graph problems.
'''
from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    def bfs(grid, start_row, start_col):
        queue = deque([(start_row, start_col, 0)])
        visited = set()

        while queue:
            row, col, distance = queue.popleft()

            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
                continue
            if (row, col) in visited or grid[row][col] == "X":
                continue

            if grid[row][col] == "C":
                return distance

            visited.add((row, col))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                queue.append((row + dr, col + dc, distance + 1))

        return -1

    return bfs(grid, starting_row, starting_col)
