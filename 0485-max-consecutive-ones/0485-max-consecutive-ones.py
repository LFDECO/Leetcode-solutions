class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        running_count=0
        for i in range(len(nums)):
            if nums[i]==0:
                running_count=0
            else:
                running_count+=1
            
            if running_count>count:
                count=running_count
        return count
            