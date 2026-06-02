class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = float("inf")
        nums.sort()
        res = None
        for i in range(len(nums)):
            anchor = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                current = anchor + nums[start] + nums[end]
                if abs(current - target) < best:
                    best = abs(current - target)
                    res = current
                if current > target:
                    end -= 1
                else:
                    start += 1
        return res
