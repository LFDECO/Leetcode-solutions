class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

    
        for ch in first:
            left = first[ch]
            right = last[ch]
            valid = True

            j = left
            while j <= right:
                curr = s[j]
                
                if first[curr] < left:
                    valid = False
                    break
                right = max(right, last[curr])
                j += 1

            if valid:
                intervals.append((right, left))

        
        intervals.sort()

        ans = []
        prev_end = -1

        for right, left in intervals:
            if left > prev_end:
                ans.append(s[left : right + 1])
                prev_end = right

        return ans