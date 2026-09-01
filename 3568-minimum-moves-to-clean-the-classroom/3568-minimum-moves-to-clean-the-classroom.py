from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        
        litter = {}
        start = None
        idx = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = idx
                    idx += 1

        if idx == 0:
            return 0

        mask = (1 << idx) - 1

        q = deque([(start[0], start[1], energy, mask)])

        visited = {
            (start[0], start[1], energy, mask)
        }

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        moves = 0

        while q:

            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

               
                if mask == 0:
                    return moves

            
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                   
                    if classroom[nr][nc] == 'R':
                        ne = energy
                    else:
                        ne = e - 1

                 
                    new_mask = mask

                    if classroom[nr][nc] == 'L':
                        litter_idx = litter[(nr, nc)]
                        new_mask &= ~(1 << litter_idx)

                    state = (nr, nc, ne, new_mask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1