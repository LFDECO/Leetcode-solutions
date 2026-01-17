class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(index,path):
            if index==len(nums):
                result.append(path.copy())
                return
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()
            if nums[index] not in path:
                backtrack(index+1,path)
        backtrack(0,[])
        return result