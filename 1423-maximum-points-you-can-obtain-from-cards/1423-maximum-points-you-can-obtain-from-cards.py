class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum1 = 0
        n = len(cardPoints)
        window = n - k
        for i in range(window):
            sum1 += cardPoints[i]
        result = sum1
        for i in range(n - k, len(cardPoints)):
            sum1 += cardPoints[i]
            sum1 -= cardPoints[i - window]
            result = min(result, sum1)
        ans = sum(cardPoints) - result
        return ans
