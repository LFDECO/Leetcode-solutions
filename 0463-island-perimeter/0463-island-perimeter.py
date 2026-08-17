class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen=set()
        row_n=len(grid)
        col_n=len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=row_n or c>=col_n:
                return 1
            if grid[r][c]==0:
                return 1
            if (r,c) in seen:
                return 0
            seen.add((r,c))
            return dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1)
        for i in range(row_n):
            for j in range(col_n):
                if grid[i][j]==1:
                    return dfs(i,j)
        