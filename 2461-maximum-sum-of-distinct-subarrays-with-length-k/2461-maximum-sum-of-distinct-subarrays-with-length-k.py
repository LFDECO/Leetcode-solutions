class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window_size = k
        window_sum = 0
        map1 = {}
        for i in range(window_size):
            window_sum += nums[i]
            if nums[i] in map1:
                map1[nums[i]] += 1
            else:
                map1[nums[i]] = 1
        if len(map1) == k:
            result = window_sum
        else:
            result = 0
        for i in range(window_size, len(nums)):
            map1[nums[i - k]] -= 1
            if map1[nums[i - k]] == 0:
                del map1[nums[i - k]]
            window_sum += nums[i]
            window_sum -= nums[i - k]
            if nums[i] in map1:
                map1[nums[i]] += 1
            else:
                map1[nums[i]] = 1
            if len(map1) == k:
                result = max(result, window_sum)
        return result
