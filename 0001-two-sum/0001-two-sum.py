class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen2 = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen2:
                return [seen2[needed], i]

            seen2[nums[i]] = i