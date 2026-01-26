class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        used=[False] * len(nums)
        def backtrack(index,path):
            if index==len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                path.append(nums[i])
                backtrack(index+1,path)
                path.pop()
                used[i]=False
        backtrack(0,[])
        return result