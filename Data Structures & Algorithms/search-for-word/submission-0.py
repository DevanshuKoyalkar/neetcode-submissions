class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        WORD_LEN = len(word)

        directions = ([1,0], [-1,0], [0,1], [0,-1])
        visited = set()

        def dfs(x, y, pos):
            if pos == WORD_LEN:
                return True

            if (x < 0 or x >= ROWS or 
                y < 0 or y >= COLUMNS or 
                board[x][y] != word[pos]):
                return False

            # Mark the current cell as visited before exploring neighbors
            temp = board[x][y]
            board[x][y] = '#'

            found = (
                dfs(x + 1, y, pos + 1) or
                dfs(x - 1, y, pos + 1) or
                dfs(x, y + 1, pos + 1) or
                dfs(x, y - 1, pos + 1)
            )
            board[x][y] = temp
            return found
        
        for i in range(ROWS):
            for j in range(COLUMNS):
                if dfs(i,j, 0):
                    return True
        
        return False
            