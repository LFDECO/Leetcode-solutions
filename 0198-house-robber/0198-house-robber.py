class Solution:
    def rob(self, nums: List[int]) -> int:
        take=0
        skip=0
        for i in range(len(nums)):
            temp=take
            take=skip+nums[i]
            skip=max(temp,skip)
        if take>skip:
            return take
        else:
            return skip

        