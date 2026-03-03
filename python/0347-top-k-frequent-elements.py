from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = dict()

        for num in nums:
            if num not in count_dict:
                count_dict[num] = 0
            else:
                count_dict[num] += 1
        
        return sorted(count_dict, key=lambda x: count_dict[x], reverse=True)[:k]