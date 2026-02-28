class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        unique=sorted(set(nums))
        nums.sort()
        for j in unique:
            for i in nums:
                if i>j and nums.count(j) != nums.count(i):
                    return [j,i]
                    break
                
        else:
            return [-1,-1]
        
