class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        s=list(s)
        while True:
            merge=False
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    if s[i]==s[j] and j-i <= k:
                        del s[j]
                        merge=True
                        break
                if merge:
                    break
                
            if  not merge:
                break
        return "".join(s)

                
        