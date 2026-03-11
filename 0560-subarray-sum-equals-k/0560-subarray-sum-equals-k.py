class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map1={}
        running_sum=0
        count=0
        map1[0]=1
        for j in range(len(nums)):
            running_sum+=nums[j]
            if running_sum-k in map1:
                count+=map1[running_sum-k]
        
            
            if running_sum in map1:
                map1[running_sum]+=1
            else:
                map1[running_sum]=1
        return count

