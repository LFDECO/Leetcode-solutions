class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map1={}
        res=[]
        for i in strs:
            sorted_str="".join(sorted(i))
            if sorted_str not in map1:
                map1[sorted_str]=[i]
            else:
                map1[sorted_str].append(i)
        for i in map1:
            res.append(map1[i])
        return res