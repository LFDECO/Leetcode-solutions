class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        ans = [1] * n
        last = [-1] * 26  # Closest ancestor for each character on current path

        def dfs(u: int) -> None:
            c = ord(s[u]) - ord('a')
            prev = last[c]
            last[c] = u

            for v in adj[u]:
                dfs(v)

            last[c] = prev  # Backtrack

            new_parent = prev if prev != -1 else parent[u]
            if new_parent != -1:
                ans[new_parent] += ans[u]

        dfs(0)
        return ans