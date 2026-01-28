class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_no=nums[0]
        for i in nums:
            if i<min_no:
                min_no=i
        return min_no
