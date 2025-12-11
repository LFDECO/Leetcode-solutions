class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new=[]
        for i in nums:
            if i not in new:
                new.append(i)
        for i in range(len(nums)):
            if i>=len(new):
                for j in range(i,len(nums)):
                    del nums[i]
                break
            nums[i]=new[i]
        
            