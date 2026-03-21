class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_size=len(p)
        map1={}
        map2={}
        result=[]
        if len(p)>len(s):
            return []
        for i in p:
            if i not in map1:
                map1[i]=1
            else:
                map1[i]+=1
        for i in range(window_size):
            if s[i] not in map2:
                map2[s[i]]=1
            else:
                map2[s[i]]+=1
        if map1==map2:
            result.append(i-window_size+1)
        for i in range(window_size,len(s)):
            if s[i] not in map2:
                map2[s[i]]=1
            else:
                map2[s[i]]+=1
            map2[s[i-window_size]]-=1
            if map2[s[i-window_size]]==0:
                del map2[s[i-window_size]]
            if map1==map2:
                result.append(i-window_size+1)
        return result

