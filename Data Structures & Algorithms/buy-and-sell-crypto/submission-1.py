class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Buy the highest number and sell at the lowest number
        and return the most game.
        """
        profit = 0
        res = 0 
        
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1,len(prices)):
                if prices[j] <= buy:
                    continue
                else:
                    sell = prices[j]
                    profit = max(profit, sell - buy)
                res = max(profit, res)
        return res