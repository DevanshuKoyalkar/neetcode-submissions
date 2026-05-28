class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # can_be_formed[i][j]
        # using first i characters of s1 and j chars of s2 form s3

        LEN1, LEN2, LEN3 = len(s1), len(s2), len(s3)

        if LEN3 != LEN1 + LEN2: 
            return False
        
        ROWS, COLS = LEN1 + 1, LEN2 + 1
        can_be_formed = [[False] * COLS for _ in range(ROWS)]

        can_be_formed[0][0] = True

        for row in range(0, ROWS):
            for col in range(0, COLS):
                pos1, pos2, pos3 = row - 1, col - 1, row + col - 1
                if row == 0 and col == 0: continue
                can_be_formed[row][col] = (
                    col > 0 and can_be_formed[row][col - 1] and s2[pos2] == s3[pos3] or 
                    row > 0 and can_be_formed[row - 1][col] and s1[pos1] == s3[pos3]
                )
        
        return can_be_formed[LEN1][LEN2]
        