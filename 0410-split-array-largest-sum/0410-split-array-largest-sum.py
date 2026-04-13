class Solution:
    def can(self, mid, k, nums):
        count = 1
        curr = 0
        for i in nums:
            if curr + i <= mid:
                curr += i
            else:
                curr = i
                count += 1
                if count > k:
                    return False
        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if self.can(mid, k, nums):
                high = mid - 1
            else:
                low = mid + 1
        return low
