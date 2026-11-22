class Solution:
    def checkString(self, s: str) -> bool:
        seen=set()
        for i in s:
            if i=='a':
                if "b" in seen:
                    return False
            seen.add(i)
        else:
            return True