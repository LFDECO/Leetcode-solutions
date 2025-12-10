class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median=0
        l3=nums1+nums2
        l3.sort()
        if(len(l3)%2==0):
            mid=len(l3)//2
            median=(l3[mid]+l3[mid-1])/2
        else:
            mid=len(l3)//2
            median=l3[mid]
        
        return median