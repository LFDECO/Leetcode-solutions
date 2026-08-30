class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=set()
        atlantic=set()
        row_n=len(heights)
        col_n=len(heights[0])
        def dfs(r,c):
            if r<0 or r>=row_n or c<0 or c>=col_n:
                return
            if (r,c) in pacific:
                return
            pacific.add((r,c))
            if 0<=r-1<row_n and 0<=c<col_n and heights[r-1][c]>=heights[r][c]:
                dfs(r-1,c)
            if 0<=r+1<row_n and 0<=c<col_n and heights[r+1][c]>=heights[r][c]:
                dfs(r+1,c)
            if 0<=r<row_n and 0<=c-1<col_n and heights[r][c-1]>=heights[r][c]:
                dfs(r,c-1)
            if 0<=r<row_n and 0<=c+1<col_n and heights[r][c+1]>=heights[r][c]:
                dfs(r,c+1)
        def dfs1(r,c):
            if r<0 or r>=row_n or c<0 or c>=col_n:
                return
            if (r,c) in atlantic:
                return
            atlantic.add((r,c))
            if 0<=r-1<row_n and 0<=c<col_n and heights[r-1][c]>=heights[r][c]:
                dfs1(r-1,c)
            if 0<=r+1<row_n and 0<=c<col_n and heights[r+1][c]>=heights[r][c]:
                dfs1(r+1,c)
            if 0<=r<row_n and 0<=c-1<col_n and heights[r][c-1]>=heights[r][c]:
                dfs1(r,c-1)
            if 0<=r<row_n and 0<=c+1<col_n and heights[r][c+1]>=heights[r][c]:
                dfs1(r,c+1)
        for i in range(row_n):
            for j in range(col_n):
                if i==0 or j==0:
                    dfs(i,j)
                if i==row_n-1 or j==col_n-1:
                    dfs1(i,j)
        res=pacific & atlantic
        res_l = [list(t) for t in res]
        return res_l
        
        