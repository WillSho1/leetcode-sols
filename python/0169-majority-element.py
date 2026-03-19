# Problem: Majority Element
# Goal: Master frequency counting or sorting to find the element that appears more than n/2 times.

# other option to use Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        majority = nums[0]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > counter[majority]:
                majority = num
        
        return majority
