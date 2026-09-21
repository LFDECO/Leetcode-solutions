class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        memo = {}

        def max_diff(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]

           
            take_left = nums[i] - max_diff(i + 1, j)
            take_right = nums[j] - max_diff(i, j - 1)

            memo[(i, j)] = max(take_left, take_right)
            return memo[(i, j)]

        return max_diff(0, len(nums) - 1) >= 0