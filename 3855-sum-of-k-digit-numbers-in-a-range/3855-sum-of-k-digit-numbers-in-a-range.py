class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        mod = 10**9+7
        m=r-l+1
        S=(l+r)*m//2
        pow_m=pow(m,k-1,mod)
        pow10k=pow(10,k,mod)
        inv9=pow(9,mod-2,mod)
        geo_sum=(pow10k-1)*inv9%mod
        return pow_m*S%mod*geo_sum%mod