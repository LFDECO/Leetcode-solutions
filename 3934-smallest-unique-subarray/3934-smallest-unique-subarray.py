class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Double rolling hash parameters to prevent hash collisions
        BASE1, MOD1 = 1315423911, 10**9 + 7
        BASE2, MOD2 = 100003, 10**9 + 9
        
        # Precompute prefix hashes and powers
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        
        for i in range(n):
            pref1[i + 1] = (pref1[i] * BASE1 + nums[i]) % MOD1
            pref2[i + 1] = (pref2[i] * BASE2 + nums[i]) % MOD2
            pow1[i + 1] = (pow1[i] * BASE1) % MOD1
            pow2[i + 1] = (pow2[i] * BASE2) % MOD2
            
        def has_unique_subarray(length: int) -> bool:
            counts = {}
            p1 = pow1[length]
            p2 = pow2[length]
            
            for i in range(n - length + 1):
                h1 = (pref1[i + length] - pref1[i] * p1) % MOD1
                h2 = (pref2[i + length] - pref2[i] * p2) % MOD2
                key = (h1 << 32) | h2
                
                if key in counts:
                    counts[key] += 1
                else:
                    counts[key] = 1
                    
            for freq in counts.values():
                if freq == 1:
                    return True
            return False

        # Binary search for the minimum valid length
        low, high = 1, n
        ans = n
        
        while low <= high:
            mid = (low + high) // 2
            if has_unique_subarray(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans