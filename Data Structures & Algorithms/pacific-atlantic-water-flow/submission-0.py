class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        # pacific 
        pacific_reachable = deque()
        pacific_visited = set()
        
        for i in range(ROWS):
            pacific_reachable.append((i,0))
            pacific_visited.add((i,0))
        
        for j in range(1, COLS):
            pacific_reachable.append((0,j))
            pacific_visited.add((0,j))

        
        while pacific_reachable:
            for _ in range(len(pacific_reachable)):
                (x, y) = pacific_reachable.popleft()

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < ROWS and 
                        0 <= ny < COLS and 
                        (nx, ny) not in pacific_visited and
                        heights[nx][ny] >= heights[x][y]
                    ):
                        pacific_visited.add((nx,ny))
                        pacific_reachable.append((nx,ny))

        # atlantic
        atlantic_reachable = deque()
        atlantic_visited = set()

        for i in range(ROWS):
            atlantic_reachable.append((i,COLS-1))
            atlantic_visited.add((i,COLS-1))
        
        for j in range(0, COLS-1):
            atlantic_reachable.append((ROWS-1,j))
            atlantic_visited.add((ROWS-1,j))

        while atlantic_reachable:
            for _ in range(len(atlantic_reachable)):
                (x, y) = atlantic_reachable.popleft()

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < ROWS and 
                        0 <= ny < COLS and 
                        (nx, ny) not in atlantic_visited and
                        heights[nx][ny] >= heights[x][y]
                    ):
                        atlantic_visited.add((nx,ny))
                        atlantic_reachable.append((nx,ny))
        print(sorted(pacific_visited))
        print(sorted(atlantic_visited))
        return list(list(pair) for pair in atlantic_visited & pacific_visited)