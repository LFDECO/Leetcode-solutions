class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, idx, val):
        while idx < len(self.tree):
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res


class Solution:
    def countSmaller(self, nums):
        ranks = {num: i + 1 for i, num in enumerate(sorted(set(nums)))}

        bit = FenwickTree(len(ranks))
        res = []

        for num in reversed(nums):
            rank = ranks[num]
            res.append(bit.query(rank - 1))
            bit.update(rank, 1)

        return res[::-1]