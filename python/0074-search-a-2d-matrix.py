from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        m = len(matrix)
        n = len(matrix[0])
        end = m*n-1

        while True:
            mid = ((end-start)//2) + start
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                start = mid + 1
            elif val > target:
                end = mid - 1
            
            if start > end:
                break
        return False 