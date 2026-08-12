class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map1={}
        n=len(nums)
        res=[]
        for i in nums:
            if i not in map1:
                map1[i]=1
            else:
                map1[i]+=1
        for i in map1:
            if map1[i]>(n/3):
                res.append(i)
        return res