class Node:
    def __init__(self, char=""):
        self.max_len = 1 if char else 0
        self.pref_len = 1 if char else 0
        self.suff_len = 1 if char else 0
        self.pref_char = char
        self.suff_char = char
        self.size = 1 if char else 0

def merge(L: Node, R: Node) -> Node:
    res = Node()
    res.size = L.size + R.size
    res.pref_char = L.pref_char
    res.suff_char = R.suff_char

    # Merge prefix
    res.pref_len = L.pref_len
    if L.pref_len == L.size and L.pref_char == R.pref_char:
        res.pref_len += R.pref_len

    # Merge suffix
    res.suff_len = R.suff_len
    if R.suff_len == R.size and R.suff_char == L.suff_char:
        res.suff_len += L.suff_len

    # Merge maximum length
    cross_len = (L.suff_len + R.pref_len) if L.suff_char == R.pref_char else 0
    res.max_len = max(L.max_len, R.max_len, cross_len)

    return res

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self._build(s, 0, 0, self.n - 1)

    def _build(self, s: str, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = Node(s[start])
            return
        mid = (start + end) // 2
        self._build(s, 2 * node + 1, start, mid)
        self._build(s, 2 * node + 2, mid + 1, end)
        self.tree[node] = merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node: int, start: int, end: int, idx: int, ch: str):
        if start == end:
            self.tree[node] = Node(ch)
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, ch)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, ch)
        self.tree[node] = merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)
        ans = []
        n = len(s)

        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(0, 0, n - 1, idx, ch)
            ans.append(st.tree[0].max_len)

        return ans