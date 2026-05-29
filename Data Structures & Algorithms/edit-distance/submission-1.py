class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        ROWS, COLS = len(word1), len(word2)

        min_dist = [[float("inf")] * (COLS+1) for _ in range(ROWS + 1)]

        for j in range(COLS + 1):
            min_dist[0][j] = j

        for i in range(ROWS + 1):
            min_dist[i][0] = i
        
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                min_dist[i][j] = 1 + min([min_dist[i][j-1], min_dist[i-1][j], min_dist[i-1][j-1]])
                if word1[i - 1] == word2[j - 1]:
                    min_dist[i][j] = min(min_dist[i][j], min_dist[i-1][j-1])
        
        # for row in min_dist:
        #     print(row)
        return min_dist[ROWS][COLS]