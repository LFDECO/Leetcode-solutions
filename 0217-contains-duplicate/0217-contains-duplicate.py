class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs=set(nums)
        if len(nums)!=len(hs):
            return True
        else:
            return False