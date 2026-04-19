class Solution:
    def solveNQueens(self, n: int):
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def is_safe(row, col):
            # same column
            for i in range(row - 1, -1, -1):
                if board[i][col] == "Q":
                    return False

            # top-left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # top-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def queens(row):
            if row == n:
                # convert board to required format
                temp = ["".join(r) for r in board]
                ans.append(temp)
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    queens(row + 1)
                    board[row][col] = "."

        queens(0)
        return ans