class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c1=0
        for i in nums:
            if len(str(i))%2==0:
                c1+=1
        return c1
