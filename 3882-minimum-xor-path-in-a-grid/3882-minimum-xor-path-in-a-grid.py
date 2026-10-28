class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [set() for _ in range(n)]
        
        for i in range(m):
            next_dp = [set() for _ in range(n)]
            for j in range(n):
                val = grid[i][j]
                if i == 0 and j == 0:
                    next_dp[0].add(val)
                    continue
                
                combined = set()
                if i > 0:
                    combined |= dp[j]
                if j > 0:
                    combined |= next_dp[j - 1]
                
                next_dp[j] = {x ^ val for x in combined}
                
            dp = next_dp
            
        return min(dp[n - 1])