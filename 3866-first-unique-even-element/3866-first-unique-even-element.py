class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in nums:
            if i%2==0 and nums.count(i)==1:
                return i
                break
        else:
            return -1