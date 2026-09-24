class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        min_idx=float('inf')
        for i in range(len(nums)):
            l=list(str(nums[i]))
            l=[int(x) for x in l]
            if sum(l)==i:
                min_idx=min(min_idx,i)
        return min_idx if min_idx !=float('inf') else -1
