class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        
        i2 = i3 = i5 = 0
        
        for i in range(1, n):
            next2 = 2 * dp[i2]
            next3 = 3 * dp[i3]
            next5 = 5 * dp[i5]
            
            dp[i] = min(next2, next3, next5)
            
            if dp[i] == next2:
                i2 += 1
            if dp[i] == next3:
                i3 += 1
            if dp[i] == next5:
                i5 += 1
        
        return dp[-1]