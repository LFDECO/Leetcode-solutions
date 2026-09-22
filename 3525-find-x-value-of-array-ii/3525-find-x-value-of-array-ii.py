class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_count = [[0] * k for _ in range(4 * self.n)]
        self._build(nums, 0, 0, self.n - 1)

    def _merge(self, p1: int, c1: list[int], p2: int, c2: list[int]):
        new_prod = (p1 * p2) % self.k
        new_count = list(c1)
        for rem in range(self.k):
            if c2[rem]:
                new_rem = (p1 * rem) % self.k
                new_count[new_rem] += c2[rem]
        return new_prod, new_count

    def _build(self, nums: list[int], node: int, l: int, r: int):
        if l == r:
            val = nums[l] % self.k
            self.tree_prod[node] = val
            self.tree_count[node][val] = 1
            return

        mid = (l + r) // 2
        left_child, right_child = 2 * node + 1, 2 * node + 2
        self._build(nums, left_child, l, mid)
        self._build(nums, right_child, mid + 1, r)

        p, c = self._merge(
            self.tree_prod[left_child], self.tree_count[left_child],
            self.tree_prod[right_child], self.tree_count[right_child]
        )
        self.tree_prod[node] = p
        self.tree_count[node] = c

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            rem = val % self.k
            self.tree_prod[node] = rem
            self.tree_count[node] = [0] * self.k
            self.tree_count[node][rem] = 1
            return

        mid = (l + r) // 2
        left_child, right_child = 2 * node + 1, 2 * node + 2
        if idx <= mid:
            self.update(left_child, l, mid, idx, val)
        else:
            self.update(right_child, mid + 1, r, idx, val)

        p, c = self._merge(
            self.tree_prod[left_child], self.tree_count[left_child],
            self.tree_prod[right_child], self.tree_count[right_child]
        )
        self.tree_prod[node] = p
        self.tree_count[node] = c

    def query(self, node: int, l: int, r: int, ql: int, qr: int):
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_count[node]

        mid = (l + r) // 2
        left_child, right_child = 2 * node + 1, 2 * node + 2

        if qr <= mid:
            return self.query(left_child, l, mid, ql, qr)
        if ql > mid:
            return self.query(right_child, mid + 1, r, ql, qr)

        p1, c1 = self.query(left_child, l, mid, ql, qr)
        p2, c2 = self.query(right_child, mid + 1, r, ql, qr)
        return self._merge(p1, c1, p2, c2)


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        seg_tree = SegmentTree(nums, k)
        n = len(nums)
        ans = []

        for idx, val, start, x in queries:
            seg_tree.update(0, 0, n - 1, idx, val)
            _, counts = seg_tree.query(0, 0, n - 1, start, n - 1)
            ans.append(counts[x])

        return ans