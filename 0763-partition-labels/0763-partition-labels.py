class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        seen=set()
        map1={}
        res=[]
        counter=0
        true_count=0
        for i in range(len(s)):
            if s[i] not in map1:
                map1[s[i]]=[i]
            else:
                map1[s[i]].append(i)
        partition_boundary=map1[s[0]][-1]
       
        while true_count<len(s):
        
            if map1[s[true_count]][-1]>partition_boundary:
                partition_boundary=map1[s[true_count]][-1]
            if true_count==partition_boundary and true_count<=len(s)-1:
                res.append(counter+1)
                if true_count+1<len(s):
                    partition_boundary=map1[s[true_count+1]][-1]
                counter=-1
            if true_count>len(s)-1:
                break
            counter+=1
            true_count+=1
        return res
