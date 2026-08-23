class Solution:

  def sumGame(self, num: str) -> bool:
    n = len(num)
    left, right = num[: n // 2], num[n // 2 :]

    left_sum = sum(int(c) for c in left if c != "?")
    right_sum = sum(int(c) for c in right if c != "?")

    left_q = left.count("?")
    right_q = right.count("?")

    
    return (left_sum - right_sum) * 2 != (right_q - left_q) * 9