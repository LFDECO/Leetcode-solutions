class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
    
        sorted_pairs = sorted((val, i) for i, val in enumerate(nums))
        
        res = [0] * n
        i = 0
        
        while i < n:
            j = i + 1
            
            while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
                j += 1
            
            group_indices = sorted(sorted_pairs[k][1] for k in range(i, j))
            
         
            for k, original_idx in enumerate(group_indices):
                res[original_idx] = sorted_pairs[i + k][0]
            
            i = j
            
        return res