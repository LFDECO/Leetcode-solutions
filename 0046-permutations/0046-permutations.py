class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(index,path):
            if index==len(nums):
                result.append(path[:])
                return
            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack(index+1,path)
                    path.pop()
        backtrack(0,[])
        return result