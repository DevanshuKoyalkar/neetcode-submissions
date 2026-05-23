class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] != '1':
                return
            
            grid[x][y] = '#'

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        def bfs(r, c):
            grid[r][c] = '#'
            queue = deque([(r, c)])
            while queue:
                (x, y) = queue.popleft()
                for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == '1':
                        grid[nx][ny] = '#'
                        queue.append((nx,ny))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    counter += 1
                    # dfs(i, j)
                    bfs(i,j)
        
        return counter
