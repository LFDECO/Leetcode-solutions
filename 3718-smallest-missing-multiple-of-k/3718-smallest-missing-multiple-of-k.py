class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums1=set(nums)
        counter=1
        while True:
            mul=k*counter
            if mul not in nums1:
                return mul
            counter+=1
