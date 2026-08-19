class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen=set()
        row_n=len(board)
        col_n=len(board[0])
        def dfs(r,c):
            if r<0 or r>=row_n or c<0 or c>=col_n:
                return
            if (r,c) in seen:
                return
            if board[r][c] == "X":
                return
            seen.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(row_n):
            for c in range(col_n):
                if r == 0 or r == row_n - 1 or c == 0 or c == col_n - 1:
                    if board[r][c]=="O":
                        dfs(r,c)
        for r in range(row_n):
            for c in range(col_n):
                if (r,c) not in seen:
                    board[r][c]="X"
        