class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 0
        last = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            added = (dp + 1 - last[idx]) % MOD
            dp = (dp + added) % MOD
            last[idx] = (last[idx] + added) % MOD

        return dp