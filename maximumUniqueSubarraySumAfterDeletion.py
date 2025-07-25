from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_set = set(nums)
        total = None

        for num in nums_set:
            if total == None:
                total = num
            else:
                total = max(num, total, total+num)
        
        return total
