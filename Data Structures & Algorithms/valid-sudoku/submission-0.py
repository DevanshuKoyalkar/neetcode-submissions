class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 rows, 9 cols, 9 boxes
        # row%3 * 3 + col%3
        LEN = 9

        rows = [set() for _ in range(LEN)]
        cols = [set() for _ in range(LEN)]
        grids = [set() for _ in range(LEN)]

        for x in range(LEN):
            for y in range(LEN):
                if board[x][y] == '.':
                    continue
                
                row_id = x
                col_id = y
                grid_id = (3 * (x//3)) + (y // 3) 

                ch = board[x][y]

                if (
                    ch in rows[row_id] or 
                    ch in cols[col_id] or
                    ch in grids[grid_id] 
                ):
                    # print(ch, x, y)
                    # print(row_id, col_id, grid_id)
                    # print(rows, cols, grids)
                    return False
                
                rows[row_id].add(ch)
                cols[col_id].add(ch)
                grids[grid_id].add(ch)
        
        return True

