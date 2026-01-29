class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_sum=nums[0]
        running_sum=0
        for i in range(len(nums)):
            if running_sum<0:
                running_sum=nums[i]
                if running_sum>final_sum:
                    final_sum=running_sum
            else:
                running_sum+=nums[i]
                if running_sum>final_sum:
                    final_sum=running_sum
        return final_sum
