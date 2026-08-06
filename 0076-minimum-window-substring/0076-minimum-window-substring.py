class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def have(map1):
            for count in map1.values():
                if count>0:
                    return False
            return True
        if len(t)>len(s):
            return ""
        res=" " * len(s)
        res=list(res)
        map1={}
        for i in t:
            if i not in map1:
                map1[i]=1
            else:
                map1[i]+=1
        left=0
        right=0
        window=[]
        while right<len(s):
            window.append(s[right])
            if s[right] in map1:
                map1[s[right]]-=1  
            while have(map1):
                if (right-left+1)<=len(res):
                    res=window[left:right+1]
                if window[left] in map1:
                    map1[window[left]]+=1
                
                left+=1
            right+=1
        
           
        if " " in res:
            return ""
        else:
            return "".join(res)

                









