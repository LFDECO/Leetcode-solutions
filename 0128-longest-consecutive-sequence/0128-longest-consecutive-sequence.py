class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set(nums)
        global_count=0
        running_count=1
        for i in hs:
            if i-1 in hs:
                pass
            else:
                running_count=1
                while i+1 in hs:
                    running_count+=1
                    i+=1
                if running_count>global_count:
                    global_count=running_count
        return global_count