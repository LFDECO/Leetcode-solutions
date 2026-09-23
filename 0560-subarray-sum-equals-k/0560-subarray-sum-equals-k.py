
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map1={}
        map1[0]=1
        running_sum=0
        count=0
        for i in nums:
            running_sum+=i
            if running_sum-k in map1:
              count+=map1[running_sum-k]
            if running_sum in map1:
                map1[running_sum]+=1
            else:
                map1[running_sum]=1
        
        return count



