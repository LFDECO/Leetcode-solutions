from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIM = 10**6 + 1

        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        half = [f // 2 for f in freq]
        mid = ""

        for i in range(26):
            if freq[i] % 2:
                mid = chr(i + ord('a'))
                break

        def count_ways(cnt):
            total = sum(cnt)
            ways = 1

            for x in cnt:
                if x:
                    ways *= comb(total, x)
                    if ways >= LIM:
                        return LIM
                    total -= x

            return ways

        if count_ways(half) < k:
            return ""

        left = []
        length = sum(half)

        for _ in range(length):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                ways = count_ways(half)

                if ways >= k:
                    left.append(chr(c + ord('a')))
                    break

                k -= ways
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]