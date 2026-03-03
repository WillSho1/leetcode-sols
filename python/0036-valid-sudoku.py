from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                # check for num
                num = board[r][c]
                if num == ".":
                    continue
                
                # check if valid
                if num in rows[r] or num in cols[c] or num in boxes[(r//3, c//3)]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r//3, c//3)].add(num)
        return True