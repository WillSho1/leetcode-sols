class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLength = 0

        for i in range(len(nums)):
            if nums[i] not in numsSet:
                continue
            count = 1
            numsSet.remove(nums[i])
            right = nums[i]+1
            while right in numsSet:
                count += 1
                numsSet.remove(right)
                right += 1
            
            left = nums[i]-1
            while left in numsSet:
                count += 1
                numsSet.remove(left)
                left -= 1
            
            maxLength = max(maxLength, count)
        
        return maxLength