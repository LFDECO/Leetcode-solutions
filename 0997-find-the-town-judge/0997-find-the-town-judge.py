class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph={}
        for i in range(1,n+1):
            graph[i]=[]
        for u,v in trust:
            graph[u].append(v)
        for i in graph:
            if graph[i]==[]:
                for j in graph:
                    if j==i:
                        continue
                    if i not in graph[j]:
                        break
                else:
                    return i
        else:
            return -1
        