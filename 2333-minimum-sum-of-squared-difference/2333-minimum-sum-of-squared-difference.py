class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)
        
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_diff = sum(diffs)
        
        # If operations exceed total diff, we can reach 0
        if total_diff <= k:
            return 0
        
        max_val = max(diffs)
        count = [0] * (max_val + 1)
        for d in diffs:
            count[d] += 1
            
        # Greedily reduce the largest values downward
        for v in range(max_val, 0, -1):
            if count[v] == 0:
                continue
            
            take = min(k, count[v])
            count[v] -= take
            count[v - 1] += take
            k -= take
            
            if k == 0:
                break
                
        return sum(v * v * c for v, c in enumerate(count))