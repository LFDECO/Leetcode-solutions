class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=[]
        stack=[]
        map1={}
        for i in nums2:
            if len(stack)==0:
                stack.append(i)
                continue
            while len(stack)>0 and i>stack[-1]:
                map1[stack[-1]]=i
                stack.pop()
            stack.append(i)
        for i in stack:
            if i not in map1:
                map1[i]=-1
        for i in nums1:
            res.append(map1[i])
        return res

