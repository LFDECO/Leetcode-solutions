class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product=1
        right_product=1
        result=[None]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                left_product=1
                result[i]=left_product
            else:
                left_product*=nums[i-1]
                result[i]=left_product
        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                right_product=1
                result[j]*=right_product
            else:
                right_product*=nums[j+1]
                result[j]*=right_product
        return result
