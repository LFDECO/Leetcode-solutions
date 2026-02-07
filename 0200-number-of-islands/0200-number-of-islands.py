class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count=0
        r=len(grid)
        c=len(grid[0])
        stack=[]
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="0":
                    pass
                else:
                    island_count+=1
                    stack.append([i,j])
                    while len(stack)!=0:
                        x,y=stack.pop()
                        if x < 0 or x >= r or y < 0 or y >= c:
                            continue
                        if grid[x][y]=="0":
                            continue
                        grid[x][y]="0"
                        stack.append([x+1,y])
                        stack.append([x-1,y])
                        stack.append([x,y+1])
                        stack.append([x,y-1])
        return island_count

                

