class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        p1=0
        p2=0
        active = 0
        for i in range(len(nums)):
            if nums[i]%2!=0:
                active = 1 - active
            if i%6==5:
                active=1-active
            if active == 0:
                p1+=nums[i]
            else:
                p2+=nums[i]
        return p1-p2