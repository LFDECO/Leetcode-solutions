class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        running_prod=1
        neg_product=1
        for i in range(len(nums)):
            temp1=neg_product
            temp2=running_prod
            neg_product=min(nums[i],temp2*nums[i],neg_product*nums[i])
            running_prod=max(nums[i],temp1*nums[i],running_prod*nums[i])
            max_prod=max(max_prod,running_prod,neg_product)
        return max_prod