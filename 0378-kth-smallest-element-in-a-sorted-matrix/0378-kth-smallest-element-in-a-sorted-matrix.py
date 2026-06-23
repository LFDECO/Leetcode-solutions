import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = [x for row in matrix for x in row]
        heapq.heapify(flat)
        for i in range(k):
            res=heapq.heappop(flat)
        return res