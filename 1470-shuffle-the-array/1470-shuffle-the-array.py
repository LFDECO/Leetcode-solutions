class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        x=nums[0:n]
        y=nums[n::]
        left,right=0,0
        while left<len(x) and right<len(y):
            res.append(x[left])
            left+=1
            res.append(y[right])
            right+=1
        while left<len(x):
            res.append(x[left])
            left+=1
        while right<len(y):
            res.append(y[right])
            right+=1
        return res

