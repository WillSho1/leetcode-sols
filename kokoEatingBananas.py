from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start_k = 1
        end_k = max(piles)
        min_k = end_k

        # binary search
        while start_k <= end_k:
            k = start_k + (end_k-start_k)//2

            # test the speed
            time = 0
            for pile in piles:
                time += -(pile//-k)

            if time <= h:
                # valid time
                min_k = min(k, min_k)
                end_k = k-1
            elif time > h:
                start_k = k+1
        
        return min_k