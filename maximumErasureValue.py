from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        total = 0
        left = 0
        unique = set()
        max_total = 0

        for right in range(len(nums)):
            # ensure unique
            while nums[right] in unique:
                unique.remove(nums[left])
                total -= nums[left]
                left += 1
            
            total += nums[right]
            unique.add(nums[right])
            max_total = max(max_total, total)
        
        return max_total