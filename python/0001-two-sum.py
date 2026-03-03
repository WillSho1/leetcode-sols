from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for ind, val in enumerate(nums):
            if target-nums[ind] in nums_dict:
                return [nums_dict[target-val], ind]
            nums_dict[nums[ind]] = ind
        return None