class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        add=0
        mul=1
        for i in n:
            add+=int(i)
            mul*=int(i)
        res=mul-add
        return res