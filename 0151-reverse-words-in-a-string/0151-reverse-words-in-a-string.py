class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s=s[::-1]
        new=""
        for i in range(len(s)):
            if i==len(s)-1:
                new+=s[i]
            else:
                new+=s[i]+" "
        return new