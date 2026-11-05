from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        cost = [0] * n
        
        sl = SortedList()

        target_l = (x + 1) // 2
        target_r = x // 2
        
        # We can maintain sum_l and sum_r dynamically:
        sum_l = 0
        sum_r = 0
        
        for i in range(n):
            val = nums[i]
            # Determine where val goes relative to current median
            if len(sl) == 0:
                sl.add(val)
                sum_l += val
            else:
                # current split point
                # Elements at indices [0, target_l - 1] belong to left half
                med = sl[min(len(sl) - 1, target_l - 1)]
                sl.add(val)
                idx = sl.bisect_left(val)
                
                # If we haven't reached window size x yet:
                if len(sl) <= target_l:
                    sum_l += val
                else:
                    if idx < target_l:
                        # Pushed into left half; element at target_l shifts to right half
                        shifted = sl[target_l]
                        sum_l += val - shifted
                        sum_r += shifted
                    else:
                        sum_r += val
            
            if i >= x:
                rem = nums[i - x]
                idx = sl.bisect_left(rem)
                if idx < target_l:
                    # Removed from left half; element at target_l (now target_l - 1) shifts to left
                    shifted = sl[target_l]
                    sum_l += shifted - rem
                    sum_r -= shifted
                else:
                    sum_r -= rem
                sl.remove(rem)

            if i >= x - 1:
                median = sl[target_l - 1]
                cost[i] = (median * target_l - sum_l) + (sum_r - median * target_r)

        # DP: Pick k non-overlapping windows of length x
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]
                if i >= x and dp[i - x][j - 1] != INF:
                    dp[i][j] = min(dp[i][j], dp[i - x][j - 1] + cost[i - 1])

        return dp[n][k]