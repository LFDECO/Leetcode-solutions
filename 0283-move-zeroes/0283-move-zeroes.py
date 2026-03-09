class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        track=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[track]
                nums[track]=nums[i]
                nums[i]=temp
                track+=1
            