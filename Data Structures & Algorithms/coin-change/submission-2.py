class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        """
        amount = 12
        remaining = keep decrementing based on value.
        i, the smallest i will be our answer.
        1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 .... to 12
        """
        memo = {}
        def dfs(i, remain):
            if i == len(coins):
                return float("inf")
            elif remain == 0:
                return 0
            elif remain < 0:
                return float("inf")

            state = (i,remain)

            if state in memo:
                return memo[state]
            take = 1 + dfs(i, remain - coins[i])
            #move to next coin
            skip = dfs(i+1,remain)
            memo[state] = min(take,skip)

            return memo[state]
            
        answer = dfs(0,amount)

        return -1 if answer == float("inf") else answer