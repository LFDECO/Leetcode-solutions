class Solution:
    def numDecodings(self, s: str) -> int:
        prev2=1
        if s[0]=="0":
            prev1=0
        else:
            prev1=1
        if len(s)==1:
            return prev1
        for i in range(1,len(s)):
            current=0
            if s[i] != "0":
                current+=prev1
            if 10<= int(s[i-1:i+1]) <=26:
                current+=prev2
            prev2=prev1
            prev1=current
        return current   

