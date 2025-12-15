class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        targ=1
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==targ:
                targ+=1
        return targ