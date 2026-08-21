from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        m = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            res = 0

            for mask in range(1, 1 << m):
                bits = 0
                cur_lcm = 1

                for i in range(m):
                    if mask & (1 << i):
                        bits += 1
                        cur_lcm = lcm(cur_lcm, coins[i])

                        if cur_lcm > x:
                            break

                if cur_lcm > x:
                    continue

                if bits & 1:
                    res += x // cur_lcm
                else:
                    res -= x // cur_lcm

            return res

        lo, hi = 1, min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo