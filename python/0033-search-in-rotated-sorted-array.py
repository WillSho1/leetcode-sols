from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = start + (end-start)//2

            if nums[mid] == target:
                return mid
            
            # min is left side
            if nums[start] > nums[mid]:
                # check if target on right
                if nums[mid] < target <= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            # min is right side
            else:
                # check if target on left
                if nums[start] <= target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
        return -1