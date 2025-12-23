class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0):
            return 0
        y=x
        for i in range(20):
            y = (y + x / y) / 2
        return int(y)