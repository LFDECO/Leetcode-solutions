class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        total=0
        i=0
        n=len(nums)
        while i<n:
            j=i
            while j<n and colors[j]==colors[i]:
                j+=1

            take=0
            skip=0
            for k in range(i,j):
                new_take=skip+nums[k]
                new_skip=max(take,skip)
                take=new_take
                skip=new_skip
            total+=max(take,skip)
            i=j
        return total
                