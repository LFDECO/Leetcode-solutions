class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hs=set(nums1)
        hs2=set(nums2)
        z=hs.intersection(hs2)
        return list(z)