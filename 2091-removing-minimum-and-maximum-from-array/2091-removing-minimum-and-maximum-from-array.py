class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_i = nums.index(min(nums))
        max_i = nums.index(max(nums))

        left = min(min_i, max_i)
        right = max(min_i, max_i)

      
        a = right + 1

        
        b = n - left

        c = (left + 1) + (n - right)

        return min(a, b, c)