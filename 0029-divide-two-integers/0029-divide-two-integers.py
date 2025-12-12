class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        result = int(dividend / divisor)

        return result
           