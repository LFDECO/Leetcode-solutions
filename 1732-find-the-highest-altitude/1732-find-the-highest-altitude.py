class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start=0
        res=[]
        res.append(start)
        for i in gain:
            res.append(start+i)
            start+=i
        return max(res)