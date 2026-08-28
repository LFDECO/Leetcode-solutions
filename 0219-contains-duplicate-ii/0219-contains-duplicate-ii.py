class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set1=set(nums)
        map1={}
        for i in set1:
            map1[i]=[]
        for i in range(len(nums)):
            map1[nums[i]].append(i)
        for i in map1:
            if len(map1[i])>=2 and abs(map1[i][0]-map1[i][1])<=k:
                return True
            if len(map1[i])>2 and abs(map1[i][1]-map1[i][2])<=k:
                return True
        else:
            return False
        
            
        