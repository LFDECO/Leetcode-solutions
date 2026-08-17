class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        bestL = [[0] * n for _ in range(n)]
        bestR = [[0] * n for _ in range(n)]

        for i in range(n):
            bestL[i][i] = stoneValue[i]
            bestR[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                l, r = i, j
                while l < r:
                    mid_sum = prefix[l + 1] - prefix[i]
                    if mid_sum * 2 >= total:
                        break
                    l += 1

                ans = 0

                if l > i:
                    ans = max(ans, bestL[i][l - 1])

                left_sum = prefix[l + 1] - prefix[i]

                if left_sum * 2 == total:
                    ans = max(
                        ans,
                        bestL[i][l],
                        bestR[l + 1][j]
                    )
                else:
                    if l < j:
                        ans = max(ans, bestR[l + 1][j])

                dp[i][j] = ans

                if i < j:
                    bestL[i][j] = max(
                        bestL[i][j - 1],
                        dp[i][j] + total
                    )

                    bestR[i][j] = max(
                        bestR[i + 1][j],
                        dp[i][j] + total
                    )

        return dp[0][n - 1]