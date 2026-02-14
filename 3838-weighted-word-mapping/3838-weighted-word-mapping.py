class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result=""
        sum1=0
        for i in words:
            for j in i:
                index=ord(j)-ord('a')
                sum1+=weights[index]
            sum1%=26
            pos=25-sum1
            result+=chr(ord('a')+pos)
            sum1=0
        return result
                