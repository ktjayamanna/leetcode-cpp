def find_first_land(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "L":
                return (row, col)  # Return immediately when found
    return None  # Return None if no land is found

grid = [
    ["W", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L"],
    ["L", "L", "L", "W", "L"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

# Using the flag approach
found = False
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "L":
            found = True
            break
    if found:
        break

print(f"First land cell found at: ({row}, {col})")
