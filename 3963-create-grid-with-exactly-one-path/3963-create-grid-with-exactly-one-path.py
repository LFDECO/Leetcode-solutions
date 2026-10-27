class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[]
        for i in range(m):
            grid.append(["#"]*n)
        for i in range(m):
            for j in range(n):
                if i==0 or j==n-1:
                    grid[i][j]="."
        for i in range(m):
            grid[i]="".join(grid[i])

        return grid