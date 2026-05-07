class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen1 = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen1:
                return [seen1[needed], i]

            seen1[nums[i]] = i