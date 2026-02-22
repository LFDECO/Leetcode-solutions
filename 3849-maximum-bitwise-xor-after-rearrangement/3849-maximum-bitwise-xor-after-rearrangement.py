class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        result =""
        count_1=0
        count_0=0
        for i in range(len(t)):
            if t[i]=="1":
                count_1+=1
            else:
                count_0+=1
        for i in range(len(s)):
            if s[i]=="0":
                if count_1>0:
                    result+="1"
                    count_1-=1
                else:
                    result+="0"
                    count_0-=1
            else:
                if count_0>0:
                    result+="1"
                    count_0-=1
                else:
                    result+="0"
                    count_1-=1
        return result
            
            