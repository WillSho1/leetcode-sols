from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price = prices[0]

        for p in prices:
            # new min price
            if p < price:
                price = p
            
            profit = max(profit, p - price)
        
        return profit