class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1={}
        result=[]
        for i in strs:
            sorted_str="".join(sorted(i))
            if sorted_str not in map1:
                map1[sorted_str]=[i]
            else:
                map1[sorted_str].append(i)
        for i in map1:
            result.append(map1[i])
        return result
