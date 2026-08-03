class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp[i % 4] stores max relative score advantage from index i
        dp = [0] * 4

        for i in range(n - 1, -1, -1):
            max_advantage = float('-inf')
            take = 0
            
            for k in range(1, 4):
                if i + k <= n:
                    take += stoneValue[i + k - 1]
                    max_advantage = max(max_advantage, take - dp[(i + k) % 4])
            
            dp[i % 4] = max_advantage

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"