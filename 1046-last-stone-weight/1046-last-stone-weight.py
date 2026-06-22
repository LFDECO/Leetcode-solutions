import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            largest = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if largest == second:
                pass
            else:
                heapq.heappush(stones, -(largest - second))
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
