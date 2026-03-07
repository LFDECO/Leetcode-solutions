class Solution:
    def missingNumber(self, nums: List[int]) -> int:
     hs=set(nums)
     n=len(nums)
     for i in range(n+1):
        if i not in hs:
            return i