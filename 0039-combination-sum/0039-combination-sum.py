class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(index,path,remaining):
            if remaining==0:
                result.append(path.copy())
                return
            if remaining<0:
                return
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,remaining-candidates[i])
                path.pop()
        backtrack(0,[],target)
        return result
        
    
