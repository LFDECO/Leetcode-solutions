class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Precompute powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(n):
            pow10[i + 1] = (pow10[i] * 10) % MOD

        # Prefix sums for digit sums and count of non-zero digits
        pref_sum = [0] * (n + 1)
        pref_cnt = [0] * (n + 1)
        
        # pref_val stores the rolling hash/value of concatenated non-zero digits
        pref_val = [0]

        for i, ch in enumerate(s):
            d = ord(ch) - 48
            pref_sum[i + 1] = pref_sum[i] + d
            pref_cnt[i + 1] = pref_cnt[i] + (1 if d != 0 else 0)
            if d != 0:
                pref_val.append((pref_val[-1] * 10 + d) % MOD)

        ans = []
        for l, r in queries:
            c1 = pref_cnt[l]
            c2 = pref_cnt[r + 1]
            k = c2 - c1

            if k == 0:
                ans.append(0)
                continue

            digit_sum = pref_sum[r + 1] - pref_sum[l]
            x = (pref_val[c2] - pref_val[c1] * pow10[k]) % MOD
            ans.append((x * digit_sum) % MOD)

        return ans