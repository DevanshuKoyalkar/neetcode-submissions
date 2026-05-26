class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # row, column and two diagonals

        #       0       1       2
        # 0     0,0     0,1     0,2
        # 1     1,0     1,1     1,2
        # 2     2,0     2,1     2,2

        # downward diagonal have the same x-y
        # upward diagnal have thee same x+y

        if not n:
            return []
        if n == 1:
            return [['Q']]

        cols = set()
        downward_diag = set()
        upward_diag = set()

        result = []
        grid = [['.'] * n for _ in range(n)]

        def dfs(row): # place queen in row
            if row == n:
                # print("came here!!")
                result.append(["".join(row) for row in grid])
                return

            for col in range(n):
                x,y = row, col
                if y in cols or x-y in downward_diag or x+y in upward_diag:
                    continue

                # print("queen placed", x, y)
                grid[x][y] = 'Q'
                cols.add(y)
                downward_diag.add(x-y)
                upward_diag.add(x+y)
            
                dfs(row + 1)
                
                grid[x][y] = '.'
                cols.remove(y)
                downward_diag.remove(x-y)
                upward_diag.remove(x+y)
    
        dfs(0)
        return result
                    


