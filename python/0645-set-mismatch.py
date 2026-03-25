class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numsSet=set()
        dup=None
        missing=None
        for num in nums:
            if num in numsSet:
                dup = num
            numsSet.add(num)
        
        for i in range(len(nums)):
            if i+1 not in numsSet:
                missing = i+1
                break
        
        return [dup, missing]