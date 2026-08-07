from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t
        c2 = c3 = c5 = c7 = 0
        temp = t
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                temp //= p
                if p == 2: c2 += 1
                elif p == 3: c3 += 1
                elif p == 5: c5 += 1
                elif p == 7: c7 += 1
        
        if temp > 1:
            return "-1"  # t has prime factors > 7

        factor_map = {
            2: (1, 0, 0, 0), 3: (0, 1, 0, 0), 4: (2, 0, 0, 0),
            5: (0, 0, 1, 0), 6: (1, 1, 0, 0), 7: (0, 0, 0, 1),
            8: (3, 0, 0, 0), 9: (0, 2, 0, 0)
        }

        @lru_cache(None)
        def min_len_needed(r2, r3, r5, r7):
            """Returns the minimum number of digits needed to cover factors (r2, r3, r5, r7)."""
            if r2 == 0 and r3 == 0 and r5 == 0 and r7 == 0:
                return 0
            
            ans = float('inf')
            # Try placing digits 9 down to 2
            for d in range(9, 1, -1):
                f2, f3, f5, f7 = factor_map[d]
                # Only try digit if it reduces at least one needed factor
                if (f2 and r2) or (f3 and r3) or (f5 and r5) or (f7 and r7):
                    nr2, nr3, nr5, nr7 = max(0, r2 - f2), max(0, r3 - f3), max(0, r5 - f5), max(0, r7 - f7)
                    ans = min(ans, 1 + min_len_needed(nr2, nr3, nr5, nr7))
            
            return ans

        def get_min_digits(r2, r3, r5, r7):
            """Reconstructs the lexicographically smallest digits multiset matching min_len_needed."""
            target_len = min_len_needed(r2, r3, r5, r7)
            if target_len == 0:
                return []
            
            # Pick smallest valid digit d (2..9) that maintains optimal path
            for d in range(2, 10):
                f2, f3, f5, f7 = factor_map[d]
                nr2, nr3, nr5, nr7 = max(0, r2 - f2), max(0, r3 - f3), max(0, r5 - f5), max(0, r7 - f7)
                if min_len_needed(nr2, nr3, nr5, nr7) == target_len - 1:
                    return [d] + get_min_digits(nr2, nr3, nr5, nr7)
            return []

        # Check if num itself is valid
        if '0' not in num:
            r2, r3, r5, r7 = c2, c3, c5, c7
            for ch in num:
                d = int(ch)
                f2, f3, f5, f7 = factor_map.get(d, (0, 0, 0, 0))
                r2, r3, r5, r7 = max(0, r2 - f2), max(0, r3 - f3), max(0, r5 - f5), max(0, r7 - f7)
            if r2 == 0 and r3 == 0 and r5 == 0 and r7 == 0:
                return num

        n = len(num)
        req_pref = [(c2, c3, c5, c7)]
        for ch in num:
            d = int(ch)
            r2, r3, r5, r7 = req_pref[-1]
            if d in factor_map:
                f2, f3, f5, f7 = factor_map[d]
                r2, r3, r5, r7 = max(0, r2 - f2), max(0, r3 - f3), max(0, r5 - f5), max(0, r7 - f7)
            req_pref.append((r2, r3, r5, r7))

        first_zero = num.find('0')
        limit_pos = n - 1 if first_zero == -1 else first_zero

        # 1. Try same length answer
        for i in range(limit_pos, -1, -1):
            cur_r2, cur_r3, cur_r5, cur_r7 = req_pref[i]
            start_digit = int(num[i]) + 1
            
            for d in range(start_digit, 10):
                f2, f3, f5, f7 = factor_map.get(d, (0, 0, 0, 0))
                nr2, nr3, nr5, nr7 = max(0, cur_r2 - f2), max(0, cur_r3 - f3), max(0, cur_r5 - f5), max(0, cur_r7 - f7)

                rem_len = n - 1 - i
                if min_len_needed(nr2, nr3, nr5, nr7) <= rem_len:
                    res = list(num[:i]) + [str(d)]
                    req_digits = get_min_digits(nr2, nr3, nr5, nr7)
                    padding_ones = rem_len - len(req_digits)
                    suffix = [1] * padding_ones + sorted(req_digits)
                    res.extend(map(str, suffix))
                    return "".join(res)

        # 2. Try longer length answer
        req_digits = get_min_digits(c2, c3, c5, c7)
        target_len = max(n + 1, len(req_digits))
        padding_ones = target_len - len(req_digits)
        ans = [1] * padding_ones + sorted(req_digits)
        return "".join(map(str, ans))