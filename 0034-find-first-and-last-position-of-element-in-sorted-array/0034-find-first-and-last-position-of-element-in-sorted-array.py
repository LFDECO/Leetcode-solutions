class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        rangel=[]
        i=0
        while(i<len(nums)):
            if nums[i]==target:
                rangel.append(i)
            i+=1
        if not rangel:
             return [-1, -1]
        return [rangel[0],rangel[-1]]