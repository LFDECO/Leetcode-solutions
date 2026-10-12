class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 1_000_000_007
        
        # Count the frequency of each bit (0 to 29)
        bit_counts = [0] * 30
        for num in nums:
            for b in range(30):
                if (num >> b) & 1:
                    bit_counts[b] += 1
        
        ans = 0
        
        # Greedily build the top k numbers
        for i in range(k):
            val = 0
            for b in range(30):
                if bit_counts[b] > 0:
                    val |= (1 << b)
                    bit_counts[b] -= 1
            
            ans = (ans + val * val) % MOD
            
        return ans