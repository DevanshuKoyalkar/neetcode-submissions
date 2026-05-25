class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # level by level bfs from all border Os at once

        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        PLACEHOLDER = '#'

        for i in range(ROWS):
            if board[i][0] == 'O':
                board[i][0] = PLACEHOLDER
                queue.append((i,0))
            if board[i][COLS-1] == 'O':
                board[i][COLS-1] = PLACEHOLDER
                queue.append((i,COLS-1))
        # print(board)
        # print(queue)
        for j in range(1, COLS - 1):
            if board[0][j] == 'O':
                board[0][j] = PLACEHOLDER
                queue.append((0, j))
            if board[ROWS-1][j] == 'O':
                board[ROWS-1][j] = PLACEHOLDER
                queue.append((ROWS-1, j))
        
        # print(board)
        # print(queue)
        while queue:
            (x,y) = queue.popleft()

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < ROWS and 0 <= ny < COLS and board[nx][ny] == 'O':
                    board[nx][ny] = PLACEHOLDER
                    queue.append((nx,ny))
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == PLACEHOLDER:
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
        