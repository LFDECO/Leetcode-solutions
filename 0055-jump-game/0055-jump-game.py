class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach=nums[0]
        for i in range(len(nums)):
            if i<=max_reach:
                max_reach = max(i+nums[i],max_reach)
            if max_reach>=len(nums)-1:
                return True
                break
        else:
            return False