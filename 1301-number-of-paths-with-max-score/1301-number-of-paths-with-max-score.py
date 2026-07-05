class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * (n + 1) for _ in range(n + 1)]
        ways = [[0] * (n + 1) for _ in range(n + 1)]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        dirs = [(1, 0), (0, 1), (1, 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue

                best = -1

                for dx, dy in dirs:
                    best = max(best, score[i + dx][j + dy])

                if best == -1:
                    continue

                score[i][j] = best

                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if score[ni][nj] == best:
                        ways[i][j] = (ways[i][j] + ways[ni][nj]) % MOD

                if board[i][j] != 'E':
                    score[i][j] += int(board[i][j])

        if ways[0][0] == 0:
            return [0, 0]

        return [score[0][0], ways[0][0]]