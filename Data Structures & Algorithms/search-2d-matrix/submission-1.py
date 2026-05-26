class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # 1 10 14
        # T T  F        target 10
        # T T  F           target 12
        # T F  F             target 5
        # invariant <=


        start, end = 0, ROWS - 1
        result_row = -1
        while start <= end:
            mid = (start + end) // 2
            # print(start, end, mid)
            if matrix[mid][0] <= target:
                result_row = mid
                start = mid + 1
            else:
                end = mid - 1
        
        start, end = 0, COLS - 1

        while start <= end:
            mid = (start + end) // 2
            if matrix[result_row][mid] == target:
                return True
            elif matrix[result_row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False