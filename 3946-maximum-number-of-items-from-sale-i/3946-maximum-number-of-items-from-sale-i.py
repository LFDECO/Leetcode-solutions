class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        # Precompute free items gained on the first purchase of item i
        free = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1
                    
        dp = [0] * (budget + 1)
        
        for i in range(n):
            cost = items[i][1]
            bonus = 1 + free[i]
            
            # 1. First purchase (0/1 Knapsack -> reverse loop)
            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + bonus)
                
            # 2. Additional purchases (Unbounded Knapsack -> forward loop)
            for b in range(cost, budget + 1):
                dp[b] = max(dp[b], dp[b - cost] + 1)
                
        return dp[budget]