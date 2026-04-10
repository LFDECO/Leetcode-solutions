import math
class Solution:
    def can(self,mid,h,piles):
        hours=0
        for i in piles:
            hours+=math.ceil(i/mid)
        if hours>h:
            return False
        else:
            return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid=low+(high-low)//2
            if self.can(mid,h,piles):
                high=mid-1
            else:
                low=mid+1
        return low



        