class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count=0
        row_n=len(grid)
        col_n=len(grid[0])
        seen=set()
        def dfs(r,c):
            if r<0 or r>=row_n or c<0 or c>=col_n:
                return 0
            if grid[r][c]==0:
                return 0
            if (r,c) in seen:
                return 0
            seen.add((r,c))
            return 1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1)
        for i in range(row_n):
            for j in range(col_n):
                if grid[i][j]==1:
                    curr_count=dfs(i,j)
                    count=max(curr_count,count)
            
        return count
        
       