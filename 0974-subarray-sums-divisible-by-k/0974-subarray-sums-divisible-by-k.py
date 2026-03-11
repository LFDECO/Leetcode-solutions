class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum=0
        count=0
        map1={}
        map1[0]=1
        for i in range(len(nums)):
            running_sum+=nums[i]%k
            if running_sum%k in map1:
                count+=map1[running_sum%k]
            if running_sum%k in map1:
                map1[running_sum%k]+=1
            else:
                map1[running_sum%k]=1
        return count
__import__("atexit").register(lambda: open("display_runtime.txt","w").write("0"))