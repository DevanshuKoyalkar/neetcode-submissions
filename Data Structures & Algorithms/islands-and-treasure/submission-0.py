class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        TREASURE = 0
        WATER = -1

        # level by level bfs from all tresures at once

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == TREASURE:
                    queue.append((i,j))
        
        distance = 0
        
        while queue:
            LEN = len(queue)
            distance += 1
            for _ in range(LEN): # we travel level by level 
                x, y = queue.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == INF:
                        grid[nx][ny] = distance
                        queue.append((nx,ny))
        

