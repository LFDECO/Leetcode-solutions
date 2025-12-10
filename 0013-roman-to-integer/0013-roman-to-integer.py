class Solution:
    def romanToInt(self, s: str) -> int:
        dicto={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num = 0
        for i in range(len(s)):
            if i+1 < len(s) and dicto[s[i]] < dicto[s[i+1]]:
                num -= dicto[s[i]]
            else:
                num+=dicto[s[i]]
        return num
