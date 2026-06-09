class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Buy the highest number and sell at the lowest number
        and return the most game.
        """
        profit = 0
        buy = float('inf')

        for p in prices:
            if buy > p:
                buy = p 
            profit = max(profit, p - buy)
        return profit
       