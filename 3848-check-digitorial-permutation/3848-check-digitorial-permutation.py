class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        def fact(n):
            if n<=1:
                return 1
        
            return n*fact(n-1)
        original_n=n
        digits=str(n)
        sum=0
        for i in digits:
            sum+=fact(int(i))
        if sorted(str(sum))==sorted(str(original_n)):
            return True
        else:
            return False
                