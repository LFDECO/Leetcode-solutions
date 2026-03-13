class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        result = window_sum / k
        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]
            result = max(result, window_sum / k)
        return result
