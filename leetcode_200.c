int is_within_bounds(int gridSize, int *gridColSize, int row, int col)
{
    if (row >= 0 && row < gridSize && col >= 0 && col < gridColSize[row])
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void dfs(char **grid, int gridSize, int *gridColSize, int row, int col)
{
    if (grid[row][col] == '-')
    {
        return;
    }
    grid[row][col] = '-';
    // dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    int row_dir[] = {1, -1, 0, 0};
    int col_dir[] = {0, 0, 1, -1};
    int num_dirs = 4;
    for (int i = 0; i < num_dirs; i++)
    {
        int new_row = row + row_dir[i];
        int new_col = col + col_dir[i];
        if (is_within_bounds(gridSize, gridColSize, new_row, new_col) == 1 && grid[new_row][new_col] != 0)
        {
            dfs(grid, gridSize, gridColSize, new_row, new_col);
        }
    }
    return;
}

int numIslands(char **grid, int gridSize, int *gridColSize)
{
    int count = 0;
    for (int row = 0; row < gridSize; row++)
    {
        for (int col = 0; col < gridColSize[row]; col++)
        {
            if (grid[row][col] != '-' && grid[row][col] != 0)
            {
                count++;
                dfs(grid, gridSize, gridColSize, row, col);
            }
        }
    }
    return count;
}