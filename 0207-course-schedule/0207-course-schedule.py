class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen=set()
        scan=set()
        graph={}
        for i in range(numCourses):
            graph[i]=[]
        for u,v in prerequisites:
            graph[v].append(u)
        def dfs(node):
            if node in scan:
                return True
            if node not in seen:
                seen.add(node)
            else:
                return False
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            else:
                scan.add(node)
                seen.remove(node)
                return True
        for i in range(0,numCourses-1):
            if not dfs(i):
                return False
        else:
            return True
