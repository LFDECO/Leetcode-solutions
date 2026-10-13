class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
      
        nums.sort(key=abs)
        
        m = len(nums) // 2  
        
        
        negative_sum = sum(x * x for x in nums[:m])
        positive_sum = sum(x * x for x in nums[m:])
        
        return positive_sum - negative_sum