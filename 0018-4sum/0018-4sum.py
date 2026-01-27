class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-1):
            anchor=nums[i]
            if i>0 and anchor==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-1):
                anchor2=nums[j]
                start=j+1
                end=len(nums)-1
                if j>i+1 and anchor2==nums[j-1]:
                    continue
                while(start<end):
                    if anchor+anchor2+nums[start]+nums[end]==target:
                        result.append([anchor,anchor2,nums[start],nums[end]])
                        start+=1
                        end-=1
                        while nums[start]==nums[start-1] and start<end:
                            start+=1
                        while nums[end]==nums[end+1] and start<end:
                            end-=1
                        
                    elif anchor+anchor2+nums[start]+nums[end]>target:
                        end-=1
                    elif anchor+anchor2+nums[start]+nums[end]<target:
                        start+=1
        return result