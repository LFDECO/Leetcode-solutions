class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        f=n-k
        if n > 2000: 
             nums[:] = nums[-k:] + nums[:-k]
             return
        else:
            for i in range(f):
                for j in range(len(nums)-1):
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp