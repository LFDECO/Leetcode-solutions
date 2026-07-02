class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        window=[]
        if len(s2) < len(s1):
            return False
        for i in range(k):
            window.append(s2[i])
        if "".join(sorted(list(s1))) in "".join(sorted(window)):
            return True
        for i in range(k,len(s2)):
            window.append(s2[i])
            window.pop(0)
            if "".join(sorted(list(s1))) in "".join(sorted(window)):
                return True
        else:
            return False
