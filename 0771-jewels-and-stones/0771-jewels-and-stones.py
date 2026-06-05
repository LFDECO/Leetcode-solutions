class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        i = 0
        j = 0
        while i < len(jewels):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    count += 1
            i += 1
        return count
