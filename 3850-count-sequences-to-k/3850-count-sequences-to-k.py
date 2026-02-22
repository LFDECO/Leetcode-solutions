from collections import defaultdict
from fractions import Fraction
class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        dp=defaultdict(int)
        dp[Fraction(1)]=1
        for x in nums:
            newdp=defaultdict(int)
            for v,count in dp.items():
                newdp[v]+=count
                newdp[v*x]+=count
                newdp[v/x]+=count
                
                
            dp=newdp
        return dp[Fraction(k)]
        