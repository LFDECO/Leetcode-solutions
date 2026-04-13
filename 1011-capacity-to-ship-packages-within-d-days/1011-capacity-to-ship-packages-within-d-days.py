class Solution:
    def can(self, mid, weights, days):
        c = 0
        d = 1
        for i in weights:
            if c + i <= mid:
                c += i
            else:
                c = i
                d += 1
                if d > days:
                    return False
        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = low + (high - low) // 2
            if self.can(mid, weights, days):
                high = mid - 1
            else:
                low = mid + 1
        return low
