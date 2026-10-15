class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        total = 0

        for i in range(n):
            distinct_elements = set()
            for j in range(i, n):
                distinct_elements.add(nums[j])
                total += len(distinct_elements) ** 2

        return total % MOD