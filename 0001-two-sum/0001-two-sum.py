class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen3 = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen3:
                return [seen3[needed], i]

            seen3[nums[i]] = i