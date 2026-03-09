# Reference: https://leetcode.com/problems/binary-search/
# Goal: Find the target value's index in an O(log N) time complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = ((right-left) // 2) + left

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle-1
            else:
                left = middle+1
        
        return -1