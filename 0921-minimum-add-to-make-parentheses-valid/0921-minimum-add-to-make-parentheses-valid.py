class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        additions_needed = 0

        for char in s:
            if char == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    additions_needed += 1

        return additions_needed + open_count