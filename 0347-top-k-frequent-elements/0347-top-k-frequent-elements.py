class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1={}
        target=1
        res=[]
        for i in nums:
            if i not in map1:
                map1[i]=1
            else:
                map1[i]+=1
        map1 = dict(sorted(map1.items(), key=lambda x: x[1], reverse=True))
        while target<=k:
            for i in map1:
                if i in res:
                    continue
                else:
                    res.append(i)
                    break
            target+=1
        return res
