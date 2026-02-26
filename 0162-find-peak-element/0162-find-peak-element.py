class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        spare=nums.copy()
        spare.sort()
        return nums.index(spare[-1])