import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # available: tracks free server IDs in sorted order
        free = SortedList(range(k))
        # busy: min-heap of (finish_time, server_id)
        busy = []
        counts = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            # Release all servers that finished before or at current arrival time
            while busy and busy[0][0] <= start:
                _, s_id = heapq.heappop(busy)
                free.add(s_id)

            if not free:
                continue  # All servers busy, request dropped

            # Target server is (i % k); find smallest available server >= target
            target = i % k
            idx = free.bisect_left(target)

            if idx < len(free):
                chosen = free[idx]
            else:
                chosen = free[0]  # Wrap around to the beginning

            counts[chosen] += 1
            free.remove(chosen)
            heapq.heappush(busy, (start + duration, chosen))

        max_req = max(counts)
        return [s for s, count in enumerate(counts) if count == max_req]