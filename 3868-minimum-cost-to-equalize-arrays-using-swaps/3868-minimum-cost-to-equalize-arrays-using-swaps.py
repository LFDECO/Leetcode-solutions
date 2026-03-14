from collections import Counter
class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        c1=Counter(nums1)
        c2=Counter(nums2)
        all_nums=set(nums1+nums2)
        moves=0
        for num in all_nums:
            total=c1[num]+c2[num]
            if total % 2 == 1:
                return -1
            diff=abs(c1[num]-c2[num])
            moves+=diff//2
        return moves//2