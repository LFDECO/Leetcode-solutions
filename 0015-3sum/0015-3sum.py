class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-1):
            anchor=nums[i]
            start=i+1
            end=len(nums)-1
            if i>0 and anchor==nums[i-1]:
                continue
            while(start<end):
                if anchor+nums[start]+nums[end]==0:
                    result.append([anchor,nums[start],nums[end]])
                    start+=1
                    end-=1
                    while nums[start]==nums[start-1] and start<end:
                        start+=1
                    while nums[end]==nums[end+1] and start<end:
                        end-=1
                    
                elif anchor+nums[start]+nums[end]>0:
                    end-=1
                elif anchor+nums[start]+nums[end]<0:
                    start+=1
        return result
            
            
