class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        # dp[r] holds the count of subarrays ending at current index with product % k == r
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            rem = num % k
            
           
            new_dp[rem] += 1
            
            for prev_rem in range(k):
                if dp[prev_rem] > 0:
                    new_rem = (prev_rem * rem) % k
                    new_dp[new_rem] += dp[prev_rem]
        
            for r in range(k):
                ans[r] += new_dp[r]
                
            dp = new_dp

        return ans