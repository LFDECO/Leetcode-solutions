from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        results = []
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                results.append(current)
                found = True

            # If we already found valid strings at this removal depth,
            # do not explore deeper levels.
            if found:
                continue

            for i, char in enumerate(current):
                if char not in ('(', ')'):
                    continue
                
                # Prune consecutive duplicates: e.g., in "((", removing either gives "("
                if i > 0 and current[i] == current[i - 1]:
                    continue

                nxt = current[:i] + current[i + 1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return results