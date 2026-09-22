class Solution:
    def maxProduct(self, n: int) -> int:
        s=str(n)
        prod=0
        left=0
        right=len(s)-1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                run_prod=int(s[i])*int(s[j])
                prod=max(run_prod,prod)
        return prod