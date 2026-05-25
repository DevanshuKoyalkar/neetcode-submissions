class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        max_island_area = 0
        island_area = 0

        
        def dfs(x, y):
            nonlocal island_area
            island_area += 1

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 1:
                    grid[nx][ny] = -1
                    dfs(nx, ny)
            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    island_area = 0
                    grid[i][j] = -1
                    dfs(i,j)
                    # print(i,j, island_area)
                    max_island_area = max(max_island_area, island_area)
        
        return max_island_area
