# Problem: Two Sum
# Goal: Master the `if target - num in my_dict:` pattern in Python.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i, num in enumerate(nums):
            if target-num in numsDict.keys():
                return [numsDict[target-num], i]
            numsDict[num] = i
        
        return None