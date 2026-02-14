class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        dicto={}
        count=0
        for i in words:
            if len(i)<k:
                continue
            else:
                prefix=i[0:k]
                if prefix in dicto:
                    dicto[prefix]+=1
                else:
                    dicto[prefix]=1
        for i in dicto:
            if dicto[i]>=2:
                count+=1
        return count
            