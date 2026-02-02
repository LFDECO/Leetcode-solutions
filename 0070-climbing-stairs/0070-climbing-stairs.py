class Solution:
    def climbStairs(self, n: int) -> int:
        first_way=0
        second_way=1
        for i in range(0,n):
            temp=first_way
            first_way=second_way
            second_way=temp+second_way
        return second_way
        