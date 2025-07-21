from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # dfs using counts of parentheses
        def _dfs(left_p, right_p, p_string):
            if left_p == n and right_p == n:
                res.append(p_string)
                return
            
            if left_p < n:
                _dfs(left_p+1, right_p, p_string+'(')


            if right_p < left_p:
                _dfs(left_p, right_p+1, p_string+')')
        
        _dfs(0, 0, '')

        return res