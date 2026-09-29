class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Total path length must be even
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # Visited states: (r, c, open_count)
        visited = set()
        
        # DFS / BFS queue
        stack = [(0, 0, 0)]
        
        while stack:
            r, c, open_cnt = stack.pop()
            
            open_cnt += 1 if grid[r][c] == '(' else -1
            
            if open_cnt < 0:
                continue
                
            remaining = (m - 1 - r) + (n - 1 - c)
            if open_cnt > remaining:
                continue
                
            if r == m - 1 and c == n - 1:
                if open_cnt == 0:
                    return True
                continue
                
            state = (r, c, open_cnt)
            if state in visited:
                continue
            visited.add(state)
            
            if r + 1 < m:
                stack.append((r + 1, c, open_cnt))
            if c + 1 < n:
                stack.append((r, c + 1, open_cnt))
                
        return False