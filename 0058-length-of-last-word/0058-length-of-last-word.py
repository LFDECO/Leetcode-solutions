class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
        new=[]
        for i in s:
            if i!="":
                new.append(i)
        return len(new[-1])