class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count=0
        visited=set()

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nei in range(len(isConnected[node])):
                if isConnected[node][nei]==1:
                    dfs(nei)
        for i in range(len(isConnected)):
            if i in visited:
                pass
            else:
                count+=1
                dfs(i)
        return count
        