class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        map1 = {}
        res = []
        for i in nums:
            if i not in map1:
                map1[i] = 1
            else:
                map1[i] += 1
        for i in map1:
            if map1[i] == 1:
                res.append(i)
        return res
