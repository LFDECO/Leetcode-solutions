class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach=nums[0]
        min_jumps=0
        curr_jump=0
        for i in range(len(nums)-1):
            if i<=max_reach:
                max_reach=max(i+nums[i],max_reach)
            if i==curr_jump or max_reach>=len(nums)-1:
                curr_jump=max_reach
                min_jumps+=1
            if max_reach>=len(nums)-1:
                break
        return min_jumps
