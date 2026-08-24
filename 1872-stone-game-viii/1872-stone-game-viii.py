class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        # Calculate prefix sums in-place or via running sum
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + stones[i]
            
        # Base case: at the last index, the player must take pref[n - 1]
        dp = pref[-1]
        
        # Traverse backwards from n - 2 down to 1
        for i in range(n - 2, 0, -1):
            dp = max(dp, pref[i] - dp)
            
        return dp