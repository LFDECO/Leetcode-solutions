class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vow=[]
        for i in s:
            if i.lower() in "aeiou":
                vow.append(i)
        
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                if len(vow)>0:
                    s[i]=vow.pop()


        

        return "".join(s)