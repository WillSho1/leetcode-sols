# Problem: Remove Element
# Goal: Master in-place list modification with O(1) extra space.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newArray = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[newArray] = nums[i]
                newArray += 1
        
        return newArray
