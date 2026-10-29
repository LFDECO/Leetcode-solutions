class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [-1] * n
        depth = [0] * n
        sz = [1] * n
        heavy = [-1] * n
        
        # 1. Iterative DFS to compute parent, depth, and subtree sizes
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)
                    
        for u in reversed(order):
            max_s = 0
            for v in adj[u]:
                if v != parent[u]:
                    sz[u] += sz[v]
                    if sz[v] > max_s:
                        max_s = sz[v]
                        heavy[u] = v
                        
        # 2. Iterative Euler Tour + Heavy-Light Decomposition (for fast LCA)
        head = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        # Stack stores (u, top_of_chain, is_entering)
        stack = [(0, 0, True)]
        while stack:
            u, h, entering = stack.pop()
            if entering:
                head[u] = h
                timer += 1
                tin[u] = timer
                stack.append((u, h, False))
                # Push light children first, then heavy child
                for v in adj[u]:
                    if v != parent[u] and v != heavy[u]:
                        stack.append((v, v, True))
                if heavy[u] != -1:
                    stack.append((heavy[u], h, True))
            else:
                tout[u] = timer

        # 3. Fenwick Tree for Range XOR Update & Point XOR Query
        bit = [0] * (n + 2)
        
        def range_xor(l: int, r: int, val: int):
            idx = l
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
            idx = r + 1
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def point_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # Fast LCA using HLD chains
        def get_lca(u: int, v: int) -> int:
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                u = parent[head[u]]
            return u if depth[u] < depth[v] else v

        # Initialize node masks and Fenwick Tree
        masks = [1 << (ord(c) - 97) for c in s]
        for u in range(n):
            range_xor(tin[u], tout[u], masks[u])
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)
                diff = masks[u] ^ new_mask
                if diff:
                    masks[u] = new_mask
                    range_xor(tin[u], tout[u], diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                path_mask = point_query(tin[u]) ^ point_query(tin[v]) ^ masks[lca]
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans