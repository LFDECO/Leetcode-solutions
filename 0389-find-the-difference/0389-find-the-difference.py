class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1=0
        sum2=0
        for i in range(len(t)):
            if i==len(s):
                sum2+=ord(t[i])
            else:
                sum1+=ord(s[i])
                sum2+=ord(t[i])
        return chr(sum2-sum1)
