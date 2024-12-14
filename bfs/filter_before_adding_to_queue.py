from collections import deque

def is_valid_move(row, col, grid, visited):
    """Check if a cell is within bounds, not visited, and not a wall."""
    return (
        0 <= row < len(grid) and
        0 <= col < len(grid[0]) and
        (row, col) not in visited and
        grid[row][col] != "X"
    )

def bfs(grid, start_row, start_col):
    """Perform BFS to find the shortest path to a carrot."""
    queue = deque([(start_row, start_col, 0)])
    visited = set()
    visited.add((start_row, start_col))  # Mark the starting point as visited

    while queue:
        row, col, distance = queue.popleft()

        # If the carrot is found, return the distance
        if grid[row][col] == "C":
            return distance

        # Explore all possible directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if is_valid_move(new_row, new_col, grid, visited):
                visited.add((new_row, new_col))  # Mark as visited when adding to the queue
                queue.append((new_row, new_col, distance + 1))

    return -1  # Return -1 if no carrot is reachable

def closest_carrot(grid, starting_row, starting_col):
    return bfs(grid, starting_row, starting_col)
