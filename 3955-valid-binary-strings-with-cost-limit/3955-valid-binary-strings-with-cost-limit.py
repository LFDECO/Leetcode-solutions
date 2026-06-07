class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res = []
        path = []
        i = 0
        cost = 0
        prev = None

        def backtrack(i, prev, cost, path):
            if i == n:
                res.append("".join(path))
                return
            path.append("0")
            backtrack(i + 1, 0, cost, path)
            path.pop()
            if prev != 1 and (cost + i) <= k:
                path.append("1")
                backtrack(i + 1, 1, cost + i, path)
                path.pop()

        backtrack(i, prev, cost, path)
        return res
