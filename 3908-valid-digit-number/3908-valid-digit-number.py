class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n1=str(n)
        x1=str(x)
        if x1 in n1 and n1[0]!=x1:
            return True
        else:
            return False