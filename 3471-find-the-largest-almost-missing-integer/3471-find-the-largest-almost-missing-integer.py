from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == 1:
            cnt = Counter(nums)
            ans = -1
            for x, f in cnt.items():
                if f == 1:
                    ans = max(ans, x)
            return ans

        if k == n:
            return max(nums)

        def unique(idx):
            for i, x in enumerate(nums):
                if i != idx and x == nums[idx]:
                    return -1
            return nums[idx]

        return max(unique(0), unique(n - 1))