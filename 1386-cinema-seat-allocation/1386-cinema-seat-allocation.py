from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Group occupied seats by row (only tracking seats 2 through 9)
        occupied = defaultdict(set)
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                occupied[row].add(col)
        
        # Start by assuming all rows can fit 2 families
        ans = 2 * n
        
        # Adjust for rows that have reserved seats
        for row, seats in occupied.items():
            left_open = not any(c in seats for c in (2, 3, 4, 5))
            right_open = not any(c in seats for c in (6, 7, 8, 9))
            mid_open = not any(c in seats for c in (4, 5, 6, 7))
            
            if left_open and right_open:
                # Can fit 2 families (no deduction needed)
                continue
            elif left_open or right_open or mid_open:
                # Can only fit 1 family (deduct 1 from the default 2)
                ans -= 1
            else:
                # Cannot fit any families (deduct 2 from the default 2)
                ans -= 2
                
        return ans