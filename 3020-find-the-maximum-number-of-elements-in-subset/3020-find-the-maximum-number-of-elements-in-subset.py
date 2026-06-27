from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_num = max(nums)

        ans = 1

        if 1 in count:
            ans = count[1]
            if ans % 2 == 0:
                ans -= 1

        for num in count:
            if num == 1:
                continue

            length = 0
            x = num

            while x <= max_num and count.get(x, 0) >= 2:
                length += 2
                x *= x

            if count.get(x, 0):
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans