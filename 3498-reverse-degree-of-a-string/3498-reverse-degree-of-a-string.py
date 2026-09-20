class Solution:
    def reverseDegree(self, s: str) -> int:
        deg=0
        for i in range(len(s)):
            deg+=(ord('z')-ord(s[i])+1)*(i+1)
        return deg