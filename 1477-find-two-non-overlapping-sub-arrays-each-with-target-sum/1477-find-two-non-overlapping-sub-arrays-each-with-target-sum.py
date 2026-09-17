class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        inf = float('inf')
        min_len = [inf] * n
        
        ans = inf
        left = 0
        current_sum = 0
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            if current_sum == target:
                curr_len = right - left + 1
                
                if left > 0 and min_len[left - 1] != inf:
                    ans = min(ans, curr_len + min_len[left - 1])
                    
                prev_best = min_len[right - 1] if right > 0 else inf
                min_len[right] = min(prev_best, curr_len)
            else:
                min_len[right] = min_len[right - 1] if right > 0 else inf
                
        return -1 if ans == inf else ans