class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res=""
        if 9*num<sum:
            return ""
        nines=sum//9
        rem=sum%9
        if nines>0:
            for i in range(nines):
                res+="9"
        if len(res)<num:
            res+=str(rem)
        while len(res)<num:
            res+="0"
        return res
