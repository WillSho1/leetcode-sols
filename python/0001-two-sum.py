# Problem: Two Sum
# Goal: Master the `if target - num in my_dict:` pattern in Python.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indMap = {}

        for i, num in enumerate(nums):
            if target-num in indMap:
                return [indMap[target-num], i]
            indMap[num] = i

        return None
