class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

       
        odd = 0
        mid = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                mid = chr(ord('a') + i)

        if odd > 1:
            return ""

        
        half = [x // 2 for x in cnt]
        n = len(s)
        m = n // 2

        prefix = []

        def possible():
            
            left = prefix[:]

            for i in range(25, -1, -1):
                left += [chr(ord('a') + i)] * half[i]

            left = ''.join(left)

            pal = left + mid + left[::-1]

            return pal > target

        for _ in range(m):

            found = False

            for c in range(26):

                if half[c] == 0:
                    continue

                half[c] -= 1
                prefix.append(chr(ord('a') + c))

                if possible():
                    found = True
                    break

                prefix.pop()
                half[c] += 1

            if not found:
                return ""

        left = ''.join(prefix)
        ans = left + mid + left[::-1]

        return ans if ans > target else ""