class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        sz = 2 * m

        T = [[0] * sz for _ in range(sz)]

        # up[x] <- sum(down[y]) for y < x
        for x in range(m):
            for y in range(x):
                T[x][m + y] = 1

        # down[x] <- sum(up[y]) for y > x
        for x in range(m):
            for y in range(x + 1, m):
                T[m + x][y] = 1

        def mat_mul(A, B):
            n1, n2, n3 = len(A), len(B), len(B[0])
            C = [[0] * n3 for _ in range(n1)]

            for i in range(n1):
                for k in range(n2):
                    if A[i][k]:
                        a = A[i][k]
                        for j in range(n3):
                            C[i][j] = (C[i][j] + a * B[k][j]) % MOD

            return C

        def mat_pow(M, p):
            R = [[int(i == j) for j in range(sz)] for i in range(sz)]

            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1

            return R

        # length = 2 base state
        state = [[0] for _ in range(sz)]

        for i in range(m):
            state[i][0] = i              # up
            state[m + i][0] = m - 1 - i # down

        P = mat_pow(T, n - 2)
        ans = mat_mul(P, state)

        return sum(row[0] for row in ans) % MOD