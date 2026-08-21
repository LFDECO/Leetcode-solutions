from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        queue = deque()
        row_n = len(grid)
        col_n = len(grid[0])
        fresh = 0
        time = 0
        for i in range(row_n):
            for j in range(col_n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    seen.add((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            shot = len(queue)
            for x in range(shot):
                r, c = queue.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < row_n and 0 <= nc < col_n and (nr, nc) not in seen:
                        if grid[nr][nc] == 1:
                            fresh -= 1
                            queue.append((nr, nc))
                            seen.add((nr, nc))
            time += 1
        if fresh > 0:
            return -1
        else:
            return time
