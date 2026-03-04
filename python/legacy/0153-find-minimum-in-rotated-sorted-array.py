from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start < end:
            mid = start + (end-start)//2

            # new list is sorted
            if nums[start] < nums[end]:
                return nums[start]
            
            # mid is min
            elif mid-1>=0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            # min in first half
            if nums[start] > nums[mid]:
                end = mid-1
            
            # mid in second half
            elif nums[mid] > nums[end]:
                start = mid+1
        
        return nums[start]

            