class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == ROTTEN:
                    queue.append((i,j))
                elif grid[i][j] == FRESH:
                    fresh_count += 1
        
        minutes_elapsed = 0

        while queue:
            if fresh_count:
                minutes_elapsed += 1
            for _ in range(len(queue)): # we travel level by level 
                x, y = queue.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == FRESH:
                        fresh_count -= 1
                        grid[nx][ny] = ROTTEN
                        queue.append((nx,ny))
        
        return minutes_elapsed if fresh_count == 0 else -1
        
