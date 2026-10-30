import heapq
from math import inf

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
    
        min_cur = [k + 1] * n
        dist = [[inf] * (k + 1) for _ in range(n)]
        
        dist[0][1] = 0
        pq = [(0, 0, 1)]  
        
        while pq:
            d, u, cur = heapq.heappop(pq)
            
            if u == n - 1:
                return d
                
            
            if d > dist[u][cur] or cur >= min_cur[u]:
                continue
            min_cur[u] = cur
            
            for v, w in adj[u]:
                nxt = 1 if labels[v] != labels[u] else cur + 1
                if nxt <= k:
                    nd = d + w
                    if nd < dist[v][nxt] and nxt < min_cur[v]:
                        dist[v][nxt] = nd
                        heapq.heappush(pq, (nd, v, nxt))
                        
        return -1