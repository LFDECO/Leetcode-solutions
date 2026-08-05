class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        nums.sort()
        start=nums[0]
        end=nums[-1]
        for i in range(start,end+1):
            if i not in nums:
                res.append(i)
        return res