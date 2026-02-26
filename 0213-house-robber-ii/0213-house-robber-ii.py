class Solution:
    def rob(self, nums: List[int]) -> int:
        take1=0
        skip1=0
        take2=0
        skip2=0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)-1):
            temp=take1
            take1=skip1+nums[i]
            skip1=max(temp,skip1)
        case1=max(take1,skip1)
        for i in range(1,len(nums)):
            temp1=take2
            take2=skip2+nums[i]
            skip2=max(temp1,skip2)
        case2=max(take2,skip2)
        return max(case1,case2)