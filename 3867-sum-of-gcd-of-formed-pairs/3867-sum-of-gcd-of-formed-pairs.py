from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        sum=0
        prefixgcd=[None]*len(nums)
        mxi=nums[0]
        for i in range(len(nums)):
            mxi=max(mxi,nums[i])
            prefixgcd[i]=gcd(nums[i],mxi)
        prefixgcd.sort()
        left=0
        right=len(prefixgcd)-1
        while(left<right):
            sum+=gcd(prefixgcd[left],prefixgcd[right])
            left+=1
            right-=1
        return sum
            