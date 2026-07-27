from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # Track the lowest price seen so far
        max_profit = 0             # Track the maximum profit
        
        for price in prices:
            # Update min_price if current price is lower
            if price < min_price:
                min_price = price
            # Calculate profit if selling today
            profit = price - min_price
            # Update max_profit if this profit is higher
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
